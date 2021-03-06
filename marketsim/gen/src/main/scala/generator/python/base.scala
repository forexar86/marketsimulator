package generator.python

import predef.PyPrintable
import predef._
import predef.Import
import predef.ImportFrom
import scala.Some

package object base {

    val tab = "    "
    val comma = ","

    abstract class Class extends gen.GenerationUnit
    {
        def name : String
        def body : Code
        def registration : Code

        private def base_classes : Code =
            if (base_class_list.isEmpty)
                TypesBound.Any_.asCode
            else
                (base_class_list map {_.asCode}).reduceLeft[Code]({ case (b, acc) => acc ||| "," ||| b })

        def base_class_list : List[TypesBound.Base] = Nil

        def code = ("# generated with " + getClass) | withImports(registration | s"class $name(" ||| base_classes ||| "):" |> body)
    }

    def withImports(code: => predef.Code) : Code =
        new WithoutImports((code.imports.toSet[Importable] map { _.repr + crlf } mkString "") + code)

    def bold(s : String) = "**" + s + "**"

    def isPrimitive(t : TypesBound.Base) = Typed.topLevel isPrimitive t.unOptionalize

    abstract class Parameter {

        val p : Typed.Parameter

        def name = p.name
        def ty = p.ty.asCode
        def initializer = p.initializer
        def s_initializer = if (initializer.nonEmpty) "= None" else ""

        def init = s"$name $s_initializer"
        def init_raw = name
        def assign =  s"self.$name = $name" ||| assign_if_none

        def assign_if_none: predef.Code =
            initializer match {
                case Some(x) => s" if $name is not None else " ||| x.asCode
                case None => ""
            }

        def comment = "" :: bold(p.name) :: (p.comment map { "\t" + _ })

        def property = s"\'$name\' : " ||| ty
        def repr = s"%($name)s"
        def call = s"self.$name"

        def setter : Code = stop
        def getter : Code = stop

        def accessors = getter | setter

        def bindEx : Code = p.ty.unOptionalize match {
            case TypesBound.List_(x) =>
                if (!isPrimitive(x))
                    s"for x in self.$name: x.$bind(self.$ctx)"
                else
                    stop
            case x if !isPrimitive(x) =>
                s"self.$name.$bind(self.$ctx)"
            case _ => stop
        }

        def reset : Code = p.ty.unOptionalize match {
            case TypesBound.List_(x) =>
                if (!isPrimitive(x))
                    s"for x in self.$name: x.reset_ex(generation)"
                else
                    stop
            case x if !isPrimitive(x) =>
                s"self.$name.reset_ex(generation)"
            case _ => stop
        }

        def register : Code = p.ty.unOptionalize match {
            case TypesBound.List_(x) =>
                if (!isPrimitive(x))
                    s"for x in self.$name: x.registerIn(registry)"
                else
                    stop
            case x if !isPrimitive(x) =>
                s"self.$name.registerIn(registry)"
            case _ => stop
        }

        def typecheck : Code = "rtti.typecheck("||| ty |||s", self.$name)"
    }

    def Def(name : String, args : Code, body : Code) = {
        val a = if (args.toString == "") "" else ", " + args
        s"def $name(self$a):" |>
                (if (body.isInstanceOf[predef.Stop]) "pass" else withImports(body)) |
        ""
    }

    def Prop(name : String, body : Code) =
        "@property" |
        s"def $name(self):" |> withImports(body) | ""

    def Getter(name : String, body : Code) = Def("get_" + name, "", body)

    def Setter(name : String, body : Code) = Def("set_" + name, "value", body)

    def Property(name : String, getter_body : Code, setter_body : Code) =
        Getter(name, getter_body) |
        Setter(name, setter_body) |
        s"$name = property(get_$name, set_$name)"

    val updateContext = "updateContext_ex"
    val bind = "bind_ex"
    val bindImpl = "bind_impl"
    val bound = "_bound_ex"
    val processing = "_processing_ex"
    val ctx = "_ctx_ex"
    val subscriptions = "_subscriptions"

    abstract class Printer extends Class {
        type Parameter <: base.Parameter
        def args        : List[String]
        def f           : Typed.Function
        def name        : String
        def docstring   : List[String]
        def alias       : String
        def category    = f.getAttribute("category")
        def registration =
            if (parameters exists { _.p.initializer.isEmpty })
                ""
            else
                s"""@registry.expose(["$category", "$alias"])""" ||| ImportFrom("registry", "marketsim")

        def join_fields(p           : Parameter => Code,
                        sep         : Code = ", ",
                        elements    : List[Parameter] = parameters) : Code
            =   Code.from(elements map p, sep)

        def mkParam(p : Typed.Parameter) : Parameter

        lazy val parameters  = f.parameters map mkParam

        lazy val parameters_non_primitive = parameters filterNot { p => isPrimitive(p.p.ty) }

        lazy val parameters_events = parameters filter { p => p.p.ty canCastTo Typed.topLevel.IEvent }

        def init_fields = join_fields({ _.init })
        def init_raw_fields = join_fields({ _.init_raw })
        def assign_fields = join_fields({ _.assign }, nl)
        def property_fields = join_fields({ _.property }, comma + nl)
        def repr_fields = join_fields({ _.repr })
        def call_fields = join_fields({ _.call })
        def accessors = join_fields({ _.accessors }, nl)

        def doc = s"""\"\"\" ${docstring.mkString(crlf)}$crlf\"\"\" """

        def init_body = assign_fields //| "rtti.check_fields(self)" ||| ImportFrom("rtti", "marketsim") | "self.typecheck()"

        def init = Def("__init__", init_fields, init_body)

        def label = if (f.tryGetAttribute("label") == Some("N/A")) stop else Prop("label", "return repr(self)")

        def label_tmpl : Code = f.tryGetAttribute("label") match {
            case Some(x) => x
            case None => alias ||| (if (parameters.isEmpty) "" else s"($repr_fields)")
        }

        def bindEx_prologue =
            s"if self.__dict__.get('$bound', False): return" |
            s"self.__dict__['$bound'] = True" |
            s"if self.__dict__.get('$processing', False):" |>
                "raise Exception('cycle detected')" |
            s"self.__dict__['$processing'] = True"

        def bindEx_epilogue : Code = s"self.__dict__['$processing'] = False"

        def bindEx_ctxCopy : Code = s"self.__dict__['$ctx'] = ctx.updatedFrom(self)"

        def bindEx_body : Code = if (parameters_non_primitive.nonEmpty) bindEx_ctxCopy else ""

        def bindEx_properties = join_fields({ _.bindEx }, nl, parameters_non_primitive)

        def bindEx_subscriptions : Code =
            s"if hasattr(self, '$subscriptions'):" |>
                s"for s in self.$subscriptions: s.$bind(self.__dict__['$ctx'])"

        def bindEx = Def(bind, "ctx", bindEx_prologue  | bindEx_body | bindEx_properties | bindEx_subscriptions | bindEx_epilogue)

        def resetEx_prologue =
            s"if self.__dict__.get('_reset_generation_ex', -1) == generation: return" |
            s"self.__dict__['_reset_generation_ex'] = generation" |
            s"if self.__dict__.get('$processing', False):" |>
                "raise Exception('cycle detected')" |
            s"self.__dict__['$processing'] = True"

        def resetEx_epilogue : Code = s"self.__dict__['$processing'] = False"

        def resetEx_body : Code = stop

        def resetEx_properties = join_fields({ _.reset }, nl, parameters_non_primitive)

        def resetEx_subscriptions : Code =
            s"if hasattr(self, '$subscriptions'):" |>
                s"for s in self.$subscriptions: s.reset_ex(generation)"

        def resetEx = Def("reset_ex", "generation", resetEx_prologue  | resetEx_body | resetEx_properties | resetEx_subscriptions | resetEx_epilogue)

        def register_prologue =
            s"if self.__dict__.get('_id', False): return" |
            s"self.__dict__['_id'] = True" |
            s"if self.__dict__.get('$processing', False):" |>
                "raise Exception('cycle detected')" |
            s"self.__dict__['$processing'] = True"

        def register_epilogue : Code = s"self.__dict__['$processing'] = False"

        def register_body : Code = "registry.insert(self)"

        def register_properties = join_fields({ _.register }, nl, parameters_non_primitive)

        def register_subscriptions : Code =
            s"if hasattr(self, '$subscriptions'):" |>
                s"for s in self.$subscriptions: s.registerIn(registry)"

        def register = Def("registerIn", "registry", register_prologue  | register_body | register_properties | register_subscriptions | register_epilogue)

        def properties = "_properties = {" |> property_fields | "}"

        def repr_body : Code = s"""return "$label_tmpl" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])"""

        def repr = Def("__repr__", "", repr_body)

        def call_body : Code = ""
        def call_args : Code = "*args, **kwargs"
        def call = Def("__call__", call_args, call_body)

        def typecheck_body =
            ImportFrom("rtti", "marketsim") |||
            join_fields( { _.typecheck }, nl)

        def typecheck = Def("typecheck", "", typecheck_body)

        def body = doc | init | label | properties | accessors | repr | bindEx | resetEx | typecheck | register
    }

    trait DocString extends Printer {
        def docstring  = f.docstring match {
            case Some(d) =>
                (bold(d.brief)  :: "" :: d.detailed) ++ ("" :: "Parameters are:" :: (parameters flatMap { _.comment }))
            case None => Nil
        }
    }

    trait Alias extends Printer {
        def alias = f.name
    }

    trait DecoratedName extends Printer {
        def name = Printer.decoratedName(f)
    }

    trait BaseClass_Function extends Printer {

        def functionBase = {
            // here should be a check that ret_type casts to some function
            if (f.ret_type canCastTo Typed.topLevel.float_) TypesBound.Nothing else f.ret_type
        }

        override def base_class_list =
            if (functionBase != TypesBound.Nothing)
                functionBase :: super.base_class_list
            else
                super.base_class_list
    }

    trait BaseClass_Observable extends Printer {

        def ty = f.ret_type.returnTypeIfFunction.get

        def trivialObservable = false

        def observableBase : TypesBound.Base =
            if (trivialObservable)
                Typed.topLevel.observableOf(ty)
            else
                Typed.topLevel.observableImplOf(ty)

        override def base_class_list = observableBase :: super.base_class_list

        override def init_body =
            observableBase.asCode ||| ".__init__(self)" |
            super.init_body
    }

    trait Intrinsic extends Printer
    {
        def impl_module : String
        def impl_function = f.name

        override def call_body : Code = s"""return $impl_module.$impl_function($call_fields)""" ||| Import(impl_module)
    }

    trait IntrinsicEx extends Printer
    {
        if (args.length != 1)
            throw new Exception(s"Annotation $name should have 1 arguments in" +
                    " form (implementation_class)" + crlf + "In function " + f)

        val last_dot_idx = args(0).lastIndexOf(".")
        val implementation_module =args(0).substring(0, last_dot_idx)
        val implementation_class  =args(0).substring(last_dot_idx + 1)

        def bindEx_internals : Code =
            s"if hasattr(self, '_internals'):" |>
                    (s"for t in self._internals:" |>
                            (s"v = getattr(self, t)" |
                            (s"if type(v) in [list, set]:" |>
                                    s"for w in v: w.$bind(self.__dict__['$ctx'])") |
                            ("else:" |>
                                    s"v.$bind(self.__dict__['$ctx'])")))


        override def bindEx_body = bindEx_ctxCopy | bindEx_internals
        override def bindEx_properties = super.bindEx_properties | s"self.$bindImpl(self.__dict__['$ctx'])"

        def resetEx_internals : Code =
            s"if hasattr(self, '_internals'):" |>
                    (s"for t in self._internals:" |>
                            (s"v = getattr(self, t)" |
                            (s"if type(v) in [list, set]:" |>
                                    s"for w in v: w.reset_ex(generation)") |
                            ("else:" |>
                                    s"v.reset_ex(generation)")))


        override def resetEx_body = resetEx_internals
        override def resetEx_properties = super.resetEx_properties | s"self.reset()"

        def register_internals : Code =
            s"if hasattr(self, '_internals'):" |>
                    (s"for t in self._internals:" |>
                            (s"v = getattr(self, t)" |
                            (s"if type(v) in [list, set]:" |>
                                    s"for w in v: w.registerIn(registry)") |
                            ("else:" |>
                                    s"v.registerIn(registry)")))


        override def register_epilogue = register_internals | super.register_epilogue
    }

    trait Bind extends Printer
    {
        def bind = Def("bind", "ctx", "self._ctx = ctx.clone()")

        override def body = super.body | bind
    }

    trait HasImpl extends Printer
    {
        def getImpl = Def("getImpl", "", "return " ||| f.body.get.asCode)

        def internals = "_internals = ['impl']"

        override def body = super.body | internals | call | reset | getImpl | getattr

        override def call_body = "return self.impl()"

        override def bindEx_body = bindEx_ctxCopy

        override def bindEx_epilogue = s"self.impl.$bind(self.__dict__['$ctx'])" | super.bindEx_epilogue

        override def resetEx_epilogue = s"self.impl.reset_ex(generation)" | super.resetEx_epilogue

        override def register_epilogue = s"self.impl.registerIn(registry)" | super.register_epilogue

        override def init_body =
            super.init_body |
            "self.impl = self.getImpl()"

        def reset = Def("reset", "",
            ("self.impl = self.getImpl()" |
            "ctx_ex = getattr(self, '_ctx_ex', None)" |
            "if ctx_ex: self.impl.bind_ex(ctx_ex)") |
            ImportFrom("context", "marketsim"))

        def getattr = Def("__getattr__", "name",
            "if name[0:2] != '__' and self.impl:" |> "return getattr(self.impl, name)" |
            "else:" |> "raise AttributeError")
    }

    trait SubscribeParameter extends Parameter
    {
        def observe_args = true

        def intrinsic_base : String

        lazy val IEvent = Typed.topLevel.getScalarBound("IEvent")

        override def setter =
            super.setter | (
            if (observe_args)
                if (p.ty canCastTo TypesBound.Optional(IEvent)) {
                    base.Def(s"on_${name}_set", "value",
                                    s"event.subscribe_field(self, '$name', value)" |||
                                    ImportFrom("event", "marketsim"))
                } else ""
            else "")
    }

    trait IntrinsicBaseClass extends Printer
    {
        Typed.topLevel.addIntrinsic(args(0), parameters map { _.p })
    }


    object python extends gen.PythonGenerator
    {
        val name = "python"

        def generatePython(/** arguments of the annotation */ args  : List[String])
                          (/** function to process         */ f     : Typed.Function) =
        {
            (if (TypesBound.isObservable(f.ret_type)) observable
                else if (f.ret_type canCastTo Typed.topLevel.ISingleAssetStrategy)
                    strategy
                else
                    function).generatePython(args)(f)
        }
    }

}
