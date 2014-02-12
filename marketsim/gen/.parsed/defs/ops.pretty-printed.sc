@category = "Ops"

package ops {@label = "-%(x)s"
    
    package  {
        // defined at defs\ops.sc: 6.9
        @python.intrinsic.observable("ops._Negate_Impl")
        def Negate(x = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 9.9
        @python.intrinsic.observable("ops._Negate_Impl")
        def Negate(x = const(1.0)) : IObservable[Float]
    }
    @label = "\\frac{%(x)s}{%(y)s}"
    
    package  {
        // defined at defs\ops.sc: 15.9
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 18.9
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = const(1.0),
                y = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 21.9
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = constant(1.0),
                y = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 24.9
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = const(1.0),
                y = constant(1.0)) : IObservable[Float]
    }
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package  {@symbol = "*"
        
        package  {
            // defined at defs\ops.sc: 33.13
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Float]
            
            // defined at defs\ops.sc: 36.13
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = const(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 39.13
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = constant(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 42.13
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = const(1.0),
                    y = constant(1.0)) : IObservable[Float]
        }
        @symbol = "+"
        
        package  {
            // defined at defs\ops.sc: 48.13
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Float]
            
            // defined at defs\ops.sc: 51.13
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = const(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 54.13
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = constant(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 57.13
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = const(1.0),
                    y = constant(1.0)) : IObservable[Float]
        }
        @symbol = "-"
        
        package  {
            // defined at defs\ops.sc: 63.13
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Float]
            
            // defined at defs\ops.sc: 66.13
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = const(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 69.13
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = constant(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 72.13
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = const(1.0),
                    y = constant(1.0)) : IObservable[Float]
        }
    }
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    package  {
        // defined at defs\ops.sc: 79.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = constant(1.0),
                      elsepart = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 84.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = const(1.0),
                      elsepart = constant(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 89.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = constant(1.0),
                      elsepart = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 94.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = const(1.0),
                      elsepart = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 99.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = side.Sell(),
                      elsepart = side.Buy()) : IFunction[Side]
        
        // defined at defs\ops.sc: 104.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = side.observableSell(),
                      elsepart = side.Buy()) : IObservable[Side]
        
        // defined at defs\ops.sc: 109.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = side.Sell(),
                      elsepart = side.observableBuy()) : IObservable[Side]
        
        // defined at defs\ops.sc: 114.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = side.observableSell(),
                      elsepart = side.observableBuy()) : IObservable[Side]
    }
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package  {
        // defined at defs\ops.sc: 124.9
        @python.intrinsic.observable("ops._Equal_Impl")
        @symbol = "=="
        def Equal(x = constant(1.0),
                  y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 128.9
        @python.intrinsic.observable("ops._NotEqual_Impl")
        @symbol = "<>"
        def NotEqual(x = constant(1.0),
                     y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 132.9
        @python.intrinsic.observable("ops._Less_Impl")
        @symbol = "<"
        def Less(x = constant(1.0),
                 y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 136.9
        @python.intrinsic.observable("ops._LessEqual_Impl")
        @symbol = "<="
        def LessEqual(x = constant(1.0),
                      y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 140.9
        @python.intrinsic.observable("ops._Greater_Impl")
        @symbol = ">"
        def Greater(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 144.9
        @python.intrinsic.observable("ops._GreaterEqual_Impl")
        @symbol = ">="
        def GreaterEqual(x = constant(1.0),
                         y = constant(1.0)) : IFunction[Boolean]
    }
}
