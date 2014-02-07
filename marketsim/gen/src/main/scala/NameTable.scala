import syntax.scala.Printer.{typed => pp}
import predef.ScPrintable
import shapeless.syntax.typeable._
import scala.collection.immutable._
import Typed.AfterTyping

package object NameTable {

    case class Scope(name       : String = "_root_",
                     parameters : List[AST.Parameter] = Nil,
                     `abstract` : Boolean = false)
            extends pp.NamesScope
            with    ScPrintable
    {
        var packages    = Map.empty[String, Scope]
        var functions   = Map.empty[String, AST.FunctionDeclaration]
        var types       = Map.empty[String, AST.TypeDeclaration]
        var attributes  = Typed.Attributes(Map.empty)
        var parent      = Option.empty[Scope]
        var typed       = Option.empty[Typed.Package]
        var bases       = List.empty[AST.QualifiedName]

        val isRoot = name == "_root_"
        val isAnonymous = name startsWith "$"
        val nonAbstract = !`abstract`

        override def equals(o : Any) = o match {
            case other : Scope =>
                name == other.name &&
                parameters == other.parameters &&
                `abstract` == other.`abstract` &&
                packages == other.packages &&
                attributes == other.attributes &&
                types == other.types &&
                bases == other.bases &&
                functions == other.functions
            case _ => false
        }

        def add(m : AST.FunctionDeclaration) {
            functions get m.name match {
                case None =>
                    check_name_is_unique(m.name, m)
                    functions = functions updated (m.name, m)
                case Some(x) =>
                    if (x != m)
                        throw new Exception(s"Trying to replace member $x\r\n by $m\r\n at $qualifiedNameAnon" )
            }
        }

        def add(t : AST.TypeDeclaration) {
            types get t.name match {
                case None =>
                    check_name_is_unique(t.name, t)
                    types = types updated (t.name, t)
                case Some(x) =>
                    if (x != t)
                        throw new Exception(s"Trying to replace type member $x\r\n by $t\r\n at $qualifiedNameAnon" )
            }
        }

        def qualifyName(x : String) : AST.QualifiedName =
            AST.QualifiedName(qualifiedName.names :+ x)

        private def getQualifiedName(show_anonymous : Boolean = false) : AST.QualifiedName =
            AST.QualifiedName(
                if (isRoot)
                    (if (show_anonymous) name else "") :: Nil
                else
                    if (isAnonymous && !show_anonymous)
                        (parent.get getQualifiedName show_anonymous).names
                    else
                        (parent.get getQualifiedName show_anonymous).names :+ name
            )

        lazy val qualifiedName     = getQualifiedName(show_anonymous = false)
        lazy val qualifiedNameAnon = getQualifiedName(show_anonymous = true)

        private def check_name_is_unique(name : String, e : Any) {
            if ((functions contains name) && functions(name) != e)
                throw new Exception(s"Duplicate definition for $name:\r\n" + functions(name) + "\r\n" + e)
            if ((types contains name) && types(name) != e)
                throw new Exception(s"Duplicate definition for $name:\r\n" + types(name) + "\r\n" + e)
            if (packages contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + packages(name) + "\r\n" + e)
        }

        def add(a : AST.Attribute) = addAttribute(a.name, a.value)

        def addAttribute(key : String, value : String) {
            attributes.items get key match {
                case None => attributes = Typed.Attributes(attributes.items updated (key, value))
                case Some(v) =>
                    if (v != value)
                        throw new Exception(s"Duplicate definition for package attribute ${qualifyName(key)}: $v => $value at $this" )
            }
        }

        private def populate(child: Scope) : Scope = {
            if (functions contains child.name)
                throw new Exception(s"Duplicate definition for ${child.name}:\r\n" + functions(child.name) + "\r\n" + child)
            packages get child.name match {
                case Some(existing) =>
                    if (existing.`abstract` != child.`abstract`)
                        throw new Exception(s"Trying to merge packages with different `abstract` annotations:" + existing + child)
                    if (existing.parameters != child.parameters)
                        throw new Exception(s"Trying to merge packages with different parameters:" + existing + child)
                    child.functions.values foreach existing.add
                    child.types.values foreach existing.add
                    child.packages.values foreach existing.populate
                    child.attributes.items foreach { p => existing.addAttribute(p._1, p._2) }
                case None =>
                    packages = packages updated(child.name, child)
                    child.parent = Some(this)
            }
            packages(child.name)
        }

        private var anon_idx = 0

        private def addImpl(p : AST.PackageDef, qn : List[String]) : Scope = qn match {
            case Nil =>
                anon_idx += 1
                addImpl(p, "$" + anon_idx :: Nil)
            case x :: Nil =>
                populate(Scope(x, p.parameters, p.`abstract`))
            case x :: tl =>
                getPackageOrCreate(x) addImpl (p, tl)
        }

        def add(p : AST.PackageDef) {
            val target = addImpl(p, if (p.name.isEmpty) Nil else p.name.get.names)
            target.bases = target.bases ++ p.bases
            create(p.members, p.attributes, target)
        }

        def removeAbstract()
        {
            packages = packages filter { _._2.nonAbstract }

            packages.values foreach { _.removeAbstract() }
        }

        def removeAnonymous()
        {
            packages.values foreach { _.removeAnonymous() }

            val (anonymous, normal) =  packages partition { _._2.isAnonymous }

            packages = normal

            anonymous.values foreach {
                pkg =>
                    pkg.packages.values foreach { inner =>
                        inner.attributes = Typed.Attributes(pkg.attributes.items ++ inner.attributes.items)
                        populate(inner)
                    }
                    pkg.functions.values foreach { m =>
                        add(m match {
                            case f : AST.FunDef =>
                                f.copy(decorators =
                                        (pkg.attributes.items map { p => AST.Attribute(p._1, p._2) }).toList
                                                ++ f.decorators)
                            case x => x
                        })
                    }
                    pkg.types.values foreach { add }
            }
        }

        def getPackageOrCreate(name : String) =
            packages get name match {
                case Some(p) => p
                case None    =>
                    val p = new Scope(name)
                    p.parent = Some(this)
                    packages = packages updated (name, p)
                    p
            }

        private def lookupPackageInnerScopes(qn : List[String]) : Option[Scope] =
        {
            //println(s"looking for $qn in inner scopes of $qualifiedNameAnon ")
            qn match {
                case x :: Nil => packages get x
                case x :: tl =>
                    packages get x map { _ lookupPackageInnerScopes tl } match {
                        case Some(y)  => y
                        case None     => None
                    }
            }
        }

        def lookupPackage(qn : List[String]) : Option[Scope] =
        {
            //println(s"looking for $qn in $qualifiedNameAnon")
            if (isAnonymous)
                parent.get lookupPackage qn
            else
                qn match {
                    case Nil => throw new Exception("Qualified name cannot be empty")
                    case "" :: tl =>
                        parent match {
                            case Some(p) => p lookupPackage qn
                            case None    => lookupPackage(tl)
                        }
                    case _ =>
                        lookupPackageInnerScopes(qn) match {
                            case Some(x) => Some(x)
                            case None    =>
                                parent flatMap { _ lookupPackage  qn }
                        }
                }
        }



        private def injectBasesImpl()
        {
            bases foreach { base =>
                 lookupPackage(base.names) match {
                     case Some(b) =>
                         b.injectBasesImpl()
                         b.functions.values filterNot { functions contains _.name } foreach { add }
                         b.types.values filterNot { types contains _.name } foreach { add }
                         b.packages.values foreach { populate }
                         b.attributes.items foreach { p => addAttribute(p._1, p._2) }
                     case None =>
                         throw new Exception(s"Cannot find base package $base for $this")
                 }
            }
            bases = Nil
        }

        def injectBases()
        {
            injectBasesImpl()
            packages.values foreach { _.injectBases() }
        }

        private def lookupTypeInnerScopes(qn : List[String]) : Option[(Scope, AST.TypeDeclaration)] =
        {
            //println(s"looking for $qn in inner scopes of $qualifiedNameAnon ")
            qn match {
                case x :: Nil =>
                    types get x map { (this, _) }
                case x :: tl =>
                    packages get x map { _ lookupTypeInnerScopes tl } match {
                        case Some(y)  => y
                        case None     => None
                    }
            }
        }


        def lookupType(qn : List[String]) : Option[(Scope, AST.TypeDeclaration)] =
        {
            //println(s"looking for $qn in $qualifiedNameAnon")
            if (isAnonymous)
                parent.get lookupType  qn
            else
                qn match {
                    case Nil => throw new Exception("Qualified name cannot be empty")
                    case "" :: tl =>
                        parent match {
                            case Some(p) => p lookupType  qn
                            case None    => lookupType(tl)
                        }
                    case _ =>
                        lookupTypeInnerScopes(qn) match {
                            case Some(x) => Some(x)
                            case None    =>
                                parent flatMap { _ lookupType  qn }
                        }
                }
        }

        private def lookupFunctionInnerScopes(qn : List[String]) : Option[(Scope, AST.FunDef)] =
        {
            //println(s"looking for $qn in inner scopes of $qualifiedNameAnon ")
            qn match {
                case x :: Nil =>
                    functions get x match {
                        case Some(f : AST.FunDef) => Some((this, f))
                        case Some(alias : AST.FunAlias) => lookupFunction(alias.target.names)
                        case None => None
                    }
                case x :: tl =>
                    packages get x map { _ lookupFunctionInnerScopes tl } match {
                        case Some(y)  => y
                        case None     => None
                    }
            }
        }


        def lookupFunction(qn : List[String]) : Option[(Scope, AST.FunDef)] =
        {
            //println(s"looking for $qn in $qualifiedNameAnon")
            if (isAnonymous)
                parent.get lookupFunction qn
            else
                qn match {
                    case Nil => throw new Exception("Qualified name cannot be empty")
                    case "" :: tl =>
                        parent match {
                            case Some(p) => p lookupFunction qn
                            case None    => lookupFunction(tl)
                        }
                    case _ =>
                        lookupFunctionInnerScopes(qn) match {
                            case Some(x) => Some(x)
                            case None    =>
                                parent flatMap { _ lookupFunction qn }
                        }
                }
        }

        def fullyQualifyType(n : AST.QualifiedName) =
            lookupType(n.names) match {
                case Some((scope, m)) => scope qualifyName m.name
                case None => throw new Exception(s"Cannot lookup $n from scope $name")
            }

        def fullyQualifyType(t : AST.Type) : AST.Type = t match {
            case AST.SimpleType(n, generics) =>
                AST.SimpleType(fullyQualifyType(n), generics map fullyQualifyType)
            case AST.TupleType(elems) => AST.TupleType(elems map fullyQualifyType)
            case AST.FunctionType(args, ret) => AST.FunctionType(args map fullyQualifyType, fullyQualifyType(ret))
            case AST.UnitType => AST.UnitType
        }


        def toTyped(target : Typed.Package) : Typed.Package =
        {
            typed = Some(target)
            packages.values foreach {
                p => p.toTyped(target.createChild(p.name, p.attributes))
            }
            target
        }
    }

    private def create(p : AST.Definitions, a : Iterable[AST.Attribute], impl : Scope) {
        p.definitions foreach {
            case t : AST.TypeDeclaration => impl.add(t)
            case m : AST.FunctionDeclaration => impl.add(m)
            case package_def : AST.PackageDef => impl.add(package_def)
        }
        a foreach { impl.add }
    }



    def create(p : List[AST.Definitions]) : Option[Scope] =
    {
        val impl : Scope = new Scope

        try {
            p foreach { create(_, Nil, impl) }

            println("\r\n\tremoving anonymous packages")
            impl.removeAnonymous()

            println("\tinjecting base packages")
            impl.injectBases()

            println("\tremoving abstract packages")
            impl.removeAbstract()

            println("\tapplying before typing annotations")
            Typed.BeforeTyping(impl)

            Some(impl)
        } catch {
            case e : Exception =>
                if (config.catch_errors) {
                    println("An error occured during building name tables:")
                    println(e.getMessage)
                    None
                }
                else throw e
        }

    }

}
