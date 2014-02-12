@category = "Ops"
package ops
{
    @label = "-%(x)s"
    package {
        @python.intrinsic.observable("ops._Negate_Impl")
        def Negate(x = constant(1.)) : IFunction[Float]

        @python.intrinsic.observable("ops._Negate_Impl")
        def Negate(x = const(1.)) : IObservable[Float]
    }

    @label = "\\frac{%(x)s}{%(y)s}"
    package {
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = constant(1.), y = constant(1.)) : IFunction[Float]

        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = const(1.), y = const(1.)) : IObservable[Float]

        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = constant(1.), y = const(1.)) : IObservable[Float]

        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = const(1.), y = constant(1.)) : IObservable[Float]
    }

    @label = "({%(x)s}{{symbol}}{%(y)s})"
    package {

        @symbol = "*"
        package {
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = constant(1.), y = constant(1.)) : IFunction[Float]

            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = const(1.), y = const(1.)) : IObservable[Float]

            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = constant(1.), y = const(1.)) : IObservable[Float]

            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = const(1.), y = constant(1.)) : IObservable[Float]
        }
    
        @symbol = "+"
        package {
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = constant(1.), y = constant(1.)) : IFunction[Float]
    
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = const(1.), y = const(1.)) : IObservable[Float]
    
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = constant(1.), y = const(1.)) : IObservable[Float]
    
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = const(1.), y = constant(1.)) : IObservable[Float]
        }
    
        @symbol = "-"
        package {
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = constant(1.), y = constant(1.)) : IFunction[Float]
    
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = const(1.), y = const(1.)) : IObservable[Float]
    
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = constant(1.), y = const(1.)) : IObservable[Float]
    
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = const(1.), y = constant(1.)) : IObservable[Float]
        }
    }

    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    package {
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond     = true() : IFunction[Boolean],
                            ifpart   = constant(1.),
                            elsepart = constant(1.)) : IFunction[Float]

        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond     = true() : IFunction[Boolean],
                            ifpart   = const(1.),
                            elsepart = constant(1.)) : IObservable[Float]

        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond     = true() : IFunction[Boolean],
                            ifpart   = constant(1.),
                            elsepart = const(1.)) : IObservable[Float]

        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond     = true() : IFunction[Boolean],
                            ifpart   = const(1.),
                            elsepart = const(1.)) : IObservable[Float]

        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond     = true() : IFunction[Boolean],
                      ifpart   = side.Sell(),
                      elsepart = side.Buy()) : IFunction[Side]

        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond     = true() : IFunction[Boolean],
                      ifpart   = side.observableSell(),
                      elsepart = side.Buy()) : IObservable[Side]

        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond     = true() : IFunction[Boolean],
                      ifpart   = side.Sell(),
                      elsepart = side.observableBuy()) : IObservable[Side]

        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond     = true() : IFunction[Boolean],
                      ifpart   = side.observableSell(),
                      elsepart = side.observableBuy()) : IObservable[Side]
    }


    @label = "({%(x)s}{{symbol}}{%(y)s})"
    package {

        @python.intrinsic.observable("ops._Equal_Impl")
        @symbol = "=="
        def Equal(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @python.intrinsic.observable("ops._NotEqual_Impl")
        @symbol = "<>"
        def NotEqual(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @python.intrinsic.observable("ops._Less_Impl")
        @symbol = "<"
        def Less(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @python.intrinsic.observable("ops._LessEqual_Impl")
        @symbol = "<="
        def LessEqual(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @python.intrinsic.observable("ops._Greater_Impl")
        @symbol = ">"
        def Greater(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @python.intrinsic.observable("ops._GreaterEqual_Impl")
        @symbol = ">="
        def GreaterEqual(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

    }

}