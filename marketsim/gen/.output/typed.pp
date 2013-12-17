
package side {
    @python.intrinsic.function("Side", "Sell", "side._Sell_Impl")
    def Sell() : () => Side
        
    
    @python.intrinsic.function("Side", "Buy", "side._Buy_Impl")
    def Buy() : () => Side
        
    
    @python.intrinsic.function("Side", "None", "side._Buy_Impl")
    def Nothing() : () => Side
        
}

package mathops {
    /** Arc tangent of x, in radians.
     *
     */
    @python.mathops("Trigonometric", "atan", "atan(%(x)s)")
    def Atan(x : IFunction = constant(0.0)) : () => Float
        
    
    /** Square root of x
     *
     */
    @python.mathops("Log/Pow", "sqrt", "\\sqrt{%(x)s}")
    def Sqrt(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Exponent of x
     *
     */
    @python.mathops("Log/Pow", "exp", "e^{%(x)s}")
    def Exp(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Natural logarithm of x (to base e)
     *
     */
    @python.mathops("Log/Pow", "log", "log(%(x)s)")
    def Log(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Return *x* raised to the power *y*.
     *
     * Exceptional cases follow Annex F of the C99 standard as far as possible.
     * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     * even when *x* is a zero or a NaN.
     * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     * ``pow(x, y)`` is undefined, and raises ``ValueError``.
     */
    @python.mathops("Log/Pow", "pow", "%(base)s^{%(power)s}")
    def Pow(base : IFunction = constant(1.0),
            power : IFunction = constant(1.0)) : () => Float
        
}

package mathutils {
    package rnd {
        /** Gamma distribution
         *
         *  Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         *
         *  The probability distribution function is: ::
         *
         *               x ** (alpha - 1) * math.exp(-x / beta)
         *     pdf(x) =  --------------------------------------
         *                  math.gamma(alpha) * beta ** alpha
         */
        @python.random()
        def gammavariate(Alpha : Float = 1.0,
                         Beta : Float = 1.0) : () => Float
            
        
        /** Normal distribution
         */
        @python.random()
        def normalvariate(/** |mu| is the mean                  */ Mu : Float = 0.0,
                          /** |sigma| is the standard deviation */ Sigma : Float = 1.0) : () => Float
            
        
        /** Pareto distribution
         */
        @python.random()
        def paretovariate(/** |alpha| is the shape parameter*/ Alpha : Float = 1.0) : () => Float
            
        
        /** Triangular distribution
         *
         * Return a random floating point number *N* such that *low* <= *N* <= *high* and
         *       with the specified *mode* between those bounds.
         *       The *low* and *high* bounds default to zero and one.
         *       The *mode* argument defaults to the midpoint between the bounds,
         *       giving a symmetric distribution.
         */
        @python.random()
        def triangular(Low : Float = 0.0,
                       High : Float = 1.0,
                       Mode : Float = 0.5) : () => Float
            
        
        /** Von Mises distribution
         */
        @python.random()
        def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu : Float = 0.0,
                            /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                              *      If |kappa| is equal to zero, this distribution reduces
                              *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa : Float = 0.0) : () => Float
            
        
        /** Uniform distribution
         *
         * Return a random floating point number *N* such that
         * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
         * The end-point value *b* may or may not be included in the range depending on
         * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
         */
        @python.random()
        def uniform(Low : Float = -10.0,
                    High : Float = 10.0) : () => Float
            
        
        /** Weibull distribution
         */
        @python.random()
        def weibullvariate(/** |alpha| is the scale parameter */ Alpha : Float = 1.0,
                           /** |beta| is the shape parameter  */ Beta : Float = 1.0) : () => Float
            
        
        /** Exponential distribution
         *
         *  Returned values range from 0 to positive infinity
         */
        @python.random()
        def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda : Float = 1.0) : () => Float
            
        
        /** Log normal distribution
         *
         * If you take the natural logarithm of this distribution,
         *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
         *  |mu| can have any value, and |sigma| must be greater than zero.
         */
        @python.random()
        def lognormvariate(Mu : Float = 0.0,
                           Sigma : Float = 1.0) : () => Float
            
        
        /** Beta distribution
         *
         * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         * Returned values range between 0 and 1.
         */
        @python.random()
        def betavariate(Alpha : Float = 1.0,
                        Beta : Float = 1.0) : () => Float
            
    }
}

package observable {
    package pricefunc {
        @python.observable("Price function", "Lp_{%(side)s}(%(book)s)")
        def LiquidityProvider(side : () => Side = side.Sell(),
                              initialValue : Float = 100.0,
                              priceDistr : () => Float = mathutils.rnd.lognormvariate(0.0,0.1),
                              book : IOrderBook = observable.orderbook.OfTrader()) : IFunction
             = observable.orderbook.SafeSidePrice(observable.orderbook.Queue(book,side),constant(initialValue))*priceDistr
    }
    
    package sidefunc {
        @python.observable("Side function", "Pt_{%(factor)s*%(dependee)s}(%(book)s)")
        def PairTrading(dependee : IOrderBook = observable.orderbook.OfTrader(),
                        factor : IFunction = constant(1.0),
                        book : IOrderBook = observable.orderbook.OfTrader()) : () => Side
             = observable.sidefunc.FundamentalValue(observable.orderbook.MidPrice(dependee)*factor,book)
        
        @python.observable("Side function", "SignalSide_{%(threshold)s}(%(signal)s)")
        def Signal(signal : IFunction = constant(),
                   threshold : Float = 0.7) : () => Side
             = if signal>const(threshold) then side.Buy() else if signal<const(0.0-threshold) then side.Sell() else side.Nothing()
        
        @python.observable("Side function", "CrAvg_{%(alpha_1)s}^{%(alpha_2)s}(%(book)s)")
        def CrossingAverages(alpha_1 : Float = 0.015,
                             alpha_2 : Float = 0.15,
                             threshold : Float = 0.0,
                             book : IOrderBook = observable.orderbook.OfTrader()) : () => Side
             = observable.sidefunc.Signal(observable.EW.Avg(observable.orderbook.MidPrice(book),alpha_1)-observable.EW.Avg(observable.orderbook.MidPrice(book),alpha_2),threshold)
        
        @python.observable("Side function", "Tf_{%(alpha)s}(%(book)s)")
        def TrendFollower(alpha : Float = 0.015,
                          threshold : Float = 0.0,
                          book : IOrderBook = observable.orderbook.OfTrader()) : () => Side
             = observable.sidefunc.Signal(Derivative(observable.EW.Avg(observable.orderbook.MidPrice(book),alpha)),threshold)
        
        @python.observable("Side function", "Fv_{%(fv)s}(%(book)s)")
        def FundamentalValue(fv : IFunction = constant(200.0),
                             book : IOrderBook = observable.orderbook.OfTrader()) : () => Side
             = if observable.orderbook.BidPrice(book)>fv then side.Sell() else if observable.orderbook.AskPrice(book)<fv then side.Buy() else side.Nothing()
        
        @python.observable("Side function", "Mr_{%(alpha)s}(%(book)s)")
        def MeanReversion(alpha : Float = 0.015,
                          book : IOrderBook = observable.orderbook.OfTrader()) : () => Side
             = observable.sidefunc.FundamentalValue(observable.EW.Avg(observable.orderbook.MidPrice(book),alpha),book)
        
        @python.observable("Side function", "Noise_{%(side_distribution)s}")
        def Noise(side_distribution : IFunction = mathutils.rnd.uniform(0.0,1.0)) : () => Side
             = if side_distribution>const(0.5) then side.Sell() else side.Buy()
    }
    
    package Cumulative {
        @python.intrinsic.function("Statistics", "Avg_{cumul}(%(source)s)", "moments.cma.CMA_Impl")
        def Avg(source : IObservable = const()) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{cumul}(%(source)s)", "moments.cmv.Variance_Impl")
        def Var(source : IObservable = const()) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}")
        def StdDev(source : IObservable = const()) : () => Float
             = mathops.Sqrt(observable.Cumulative.Var(source))
        
        @python.function("Statistics", "RSD_{cumul}_{%(source)s}")
        def RelStdDev(source : IObservable = const()) : IObservable
             = (source-observable.Cumulative.Avg(source))/observable.Cumulative.StdDev(source)
    }
    
    package rsi {
        @python.observable("RSI", "RSI-raw_{%(timeframe)s}^{%(alpha)s}(%(source)s)")
        def Raw(source : IObservable = observable.orderbook.MidPrice(),
                timeframe : Float = 10.0,
                alpha : Float = 0.015) : IFunction
             = observable.EW.Avg(observable.UpMovements(source,timeframe),alpha)/observable.EW.Avg(observable.DownMovements(source,timeframe),alpha)
    }
    
    package macd {
        @python.function("MACD", "MACD_{%(fast)s}^{%(slow)s}(%(x)s)")
        def MACD(x : IObservable = observable.orderbook.MidPrice(),
                 slow : Float = 26.0,
                 fast : Float = 12.0) : IFunction
             = observable.EW.Avg(x,2.0/(fast+1.0))-observable.EW.Avg(x,2.0/(slow+1.0))
        
        @python.function("MACD", "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
        def Signal(x : IObservable = observable.orderbook.MidPrice(),
                   slow : Float = 26.0,
                   fast : Float = 12.0,
                   timeframe : Float = 9.0,
                   step : Float = 1.0) : IDifferentiable
             = observable.EW.Avg(observable.OnEveryDt(step,observable.macd.MACD(x,slow,fast)),2.0/(timeframe+1.0))
        
        @python.function("MACD", "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
        def Histogram(x : IObservable = observable.orderbook.MidPrice(),
                      slow : Float = 26.0,
                      fast : Float = 12.0,
                      timeframe : Float = 9.0,
                      step : Float = 1.0) : IFunction
             = observable.macd.MACD(x,slow,fast)-observable.macd.Signal(x,slow,fast,timeframe,step)
    }
    
    package trader {
        @python.intrinsic.observable("Trader's", "Balance_{%(trader)s}", "trader.props.Balance_Impl")
        def Balance(trader : ISingleAssetTrader = observable.trader.SingleProxy()) : () => Float
            
        
        @python.intrinsic.observable("Trader's", "Amount_{%(trader)s}", "trader.props.Position_Impl")
        def Position(trader : ISingleAssetTrader = observable.trader.SingleProxy()) : () => Float
            
        
        @python.observable("Trader's", "Efficiency_{%(trader)s}")
        def Efficiency(trader : ISingleAssetTrader = observable.trader.SingleProxy()) : IFunction
             = observable.trader.Balance(trader)+observable.orderbook.CumulativePrice(observable.orderbook.OfTrader(trader),observable.trader.Position(trader))
        
        @python.intrinsic.function("Proxies", "N/A", "trader.proxy._Single_Impl")
        def SingleProxy() : ISingleAssetTrader
            
        
        @python.function("Trader's", "EfficiencyTrend_{%(trader)s}")
        def EfficiencyTrend(trader : ISingleAssetTrader = observable.trader.SingleProxy(),
                            alpha : Float = 0.15) : () => Float
             = Derivative(observable.EW.Avg(observable.trader.Efficiency(trader),alpha))
        
        @python.intrinsic.observable("Trader's", "PendingVolume_{%(trader)s}", "trader.props.PendingVolume_Impl")
        def PendingVolume(trader : ISingleAssetTrader = observable.trader.SingleProxy()) : () => Float
            
    }
    
    package volumefunc {
        @python.observable("Volume function", "Dp_{%(trader)s}(%(desiredPosition)s)")
        def DesiredPosition(desiredPosition : IObservable = const(),
                            trader : ISingleAssetTrader = observable.trader.SingleProxy()) : IObservable
             = desiredPosition-observable.trader.Position(trader)-observable.trader.PendingVolume(trader)
        
        @python.observable("Volume function", "Bl_{%(trader)s}(%(alpha)s)*%(k)s")
        def Bollinger_linear(alpha : Float = 0.15,
                             k : IObservable = const(0.5),
                             trader : ISingleAssetTrader = observable.trader.SingleProxy()) : IObservable
             = observable.volumefunc.DesiredPosition(observable.OnEveryDt(1.0,observable.EW.RelStdDev(observable.orderbook.MidPrice(observable.orderbook.OfTrader(trader)),alpha))*k,trader)
        
        @python.observable("Volume function", "RSI_{%(trader)s}(%(alpha)s, %(timeframe)s)*%(k)s")
        def RSI_linear(alpha : Float = 1.0/14.0,
                       k : IObservable = const(-0.04),
                       timeframe : Float = 1.0,
                       trader : ISingleAssetTrader = observable.trader.SingleProxy()) : IObservable
             = observable.volumefunc.DesiredPosition(observable.OnEveryDt(1.0,const(50.0)-observable.RSI(observable.orderbook.OfTrader(trader),timeframe,alpha))*k,trader)
    }
    
    package EW {
        @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "moments.ewma.EWMA_Impl")
        def Avg(source : IFunction = constant(),
                alpha : Float = 0.015) : IDifferentiable
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}", "moments.ewmv.EWMV_Impl")
        def Var(source : IObservable = const(),
                alpha : Float = 0.015) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}")
        def StdDev(source : IObservable = const(),
                   alpha : Float = 0.015) : () => Float
             = mathops.Sqrt(observable.EW.Var(source,alpha))
        
        @python.function("Statistics", "RSD_{\\alpha=%(alpha)s}_{%(source)s}")
        def RelStdDev(source : IObservable = const(),
                      alpha : Float = 0.15) : IObservable
             = (source-observable.EW.Avg(source,alpha))/observable.EW.StdDev(source,alpha)
    }
    
    package orderbook {
        @python.observable("Orderbook", "SafeSidePrice^{%(queue)s}")
        def SafeSidePrice(queue : IOrderQueue = observable.orderbook.Asks(),
                          defaultValue : IFunction = constant(100.0)) : IFunction
             = IfDefined(observable.orderbook.BestPrice(queue),IfDefined(observable.orderbook.LastPrice(queue),defaultValue))
        
        def PriceAtVolume(queue : IOrderQueue = observable.orderbook.Asks(),
                          volume : Float = 100.0) : () => Float
            
        
        @python.observable("Orderbook", "Price_{%(alpha)s}^{%(queue)s}")
        def WeightedPrice(queue : IOrderQueue = observable.orderbook.Asks(),
                          alpha : Float = 0.015) : IFunction
             = observable.EW.Avg(observable.orderbook.LastTradePrice(queue)*observable.orderbook.LastTradeVolume(queue),alpha)/observable.EW.Avg(observable.orderbook.LastTradeVolume(queue),alpha)
        
        def TickSize(book : IOrderBook = observable.orderbook.OfTrader()) : () => Float
            
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskLastPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
             = observable.orderbook.LastPrice(observable.orderbook.Asks(book))
        
        @python.observable("Orderbook", "Ask_{%(alpha)s}^{%(book)s}")
        def AskWeightedPrice(book : IOrderBook = observable.orderbook.OfTrader(),
                             alpha : Float = 0.015) : IFunction
             = observable.orderbook.WeightedPrice(observable.orderbook.Asks(book),alpha)
        
        @python.observable("Orderbook", "MidPrice_{%(book)s}")
        def MidPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
             = (observable.orderbook.AskPrice(book)+observable.orderbook.BidPrice(book))/const(2.0)
        
        @python.intrinsic.function("Asset's", "Asks(%(book)s)", "orderbook.queue._Asks_Impl")
        def Asks(book : IOrderBook = observable.orderbook.OfTrader()) : IOrderQueue
             = observable.orderbook.Queue(book,side.Sell())
        
        @python.observable("Orderbook", "Bid_{%(alpha)s}^{%(book)s}")
        def BidWeightedPrice(book : IOrderBook = observable.orderbook.OfTrader(),
                             alpha : Float = 0.015) : IFunction
             = observable.orderbook.WeightedPrice(observable.orderbook.Bids(book),alpha)
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
             = observable.orderbook.BestPrice(observable.orderbook.Asks(book))
        
        @python.intrinsic.observable("Orderbook", "LastTradeVolume(%(queue)s)", "orderbook.last_trade._LastTradeVolume_Impl")
        def LastTradeVolume(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
             = observable.orderbook.BestPrice(observable.orderbook.Bids(book))
        
        @python.intrinsic.function("Asset's", "Bids(%(book)s)", "orderbook.queue._Bids_Impl")
        def Bids(book : IOrderBook = observable.orderbook.OfTrader()) : IOrderQueue
             = observable.orderbook.Queue(book,side.Buy())
        
        @python.intrinsic.observable("Orderbook", "Price(%(queue)s)", "orderbook.props._BestPrice_Impl")
        def BestPrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.intrinsic.function("Asset's", "Queue(%(book)s)", "orderbook.queue._Queue_Impl")
        def Queue(book : IOrderBook = observable.orderbook.OfTrader(),
                  side : () => Side = side.Sell()) : IOrderQueue
            
        
        @python.intrinsic.function("Proxies", "N/A", "orderbook.of_trader._OfTrader_Impl")
        def OfTrader(Trader : ISingleAssetTrader = observable.trader.SingleProxy()) : IOrderBook
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidLastPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
             = observable.orderbook.LastPrice(observable.orderbook.Bids(book))
        
        @python.intrinsic.observable("Orderbook", "CumulativePrice(%(book)s, %(depth)s)", "orderbook.cumulative_price.CumulativePrice_Impl")
        def CumulativePrice(book : IOrderBook = observable.orderbook.OfTrader(),
                            depth : IFunction = constant()) : () => Float
            
        
        @python.intrinsic.observable("Orderbook", "LastPrice(%(queue)s)", "orderbook.last_price._LastPrice_Impl")
        def LastPrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Spread_{%(book)s}")
        def Spread(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
             = observable.orderbook.AskPrice(book)-observable.orderbook.BidPrice(book)
        
        @python.intrinsic.observable("Orderbook", "LastTradePrice(%(queue)s)", "orderbook.last_trade._LastTradePrice_Impl")
        def LastTradePrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
    }
    
    package Moving {
        @python.intrinsic.function("Statistics", "Avg_{n=%(timeframe)s}(%(source)s)", "moments.ma.MA_Impl")
        def Avg(source : IObservable = const(),
                timeframe : Float = 100.0) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{n=%(timeframe)s}(%(source)s)", "moments.mv.MV_Impl")
        def Var(source : IObservable = const(),
                timeframe : Float = 100.0) : IFunction
             = observable.Max(const(0.0),observable.Moving.Avg(source*source,timeframe)-observable.Sqr(observable.Moving.Avg(source,timeframe)))
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}")
        def StdDev(source : IObservable = const(),
                   timeframe : Float = 100.0) : () => Float
             = mathops.Sqrt(observable.Moving.Var(source))
        
        @python.function("Statistics", "RSD_{n=%(timeframe)s}_{%(source)s}")
        def RelStdDev(source : IObservable = const(),
                      timeframe : Float = 100.0) : IObservable
             = (source-observable.Moving.Avg(source,timeframe))/observable.Moving.StdDev(source,timeframe)
    }
    
    @python.intrinsic.observable("Basic", "[%(x)s]_dt=%(dt)s", "observable.on_every_dt._OnEveryDt_Impl")
    def OnEveryDt(dt : Float = 1.0,
                  x : IFunction = constant()) : IObservable
        
    
    @python.observable("Basic", "min{%(x)s, %(y)s}")
    def Min(x : IFunction = constant(),
            y : IFunction = constant()) : IFunction
         = if x<y then x else y
    
    @python.observable("RSI", "Downs_{%(timeframe)s}(%(source)s)")
    def DownMovements(source : IObservable = observable.orderbook.MidPrice(),
                      timeframe : Float = 10.0) : IFunction
         = observable.Max(const(0.0),observable.Lagged(source,timeframe)-source)
    
    @python.intrinsic.observable("Basic", "Lagged_{%(timeframe)s}(%(source)s)", "observable.lagged.Lagged_Impl")
    def Lagged(source : IObservable = const(),
               timeframe : Float = 10.0) : IObservable
        
    
    @python.observable("Basic", "max{%(x)s, %(y)s}")
    def Max(x : IFunction = constant(),
            y : IFunction = constant()) : IFunction
         = if x>y then x else y
    
    @python.observable("RSI", "Ups_{%(timeframe)s}(%(source)s)")
    def UpMovements(source : IObservable = observable.orderbook.MidPrice(),
                    timeframe : Float = 10.0) : IFunction
         = observable.Max(const(0.0),source-observable.Lagged(source,timeframe))
    
    @python.observable("Pow/Log", "{%(x)s}^2")
    def Sqr(x : IFunction = constant()) : IFunction
         = x*x
    
    @python.observable("RSI", "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)")
    def RSI(book : IOrderBook = observable.orderbook.OfTrader(),
            timeframe : Float = 10.0,
            alpha : Float = 0.015) : IObservable
         = const(100.0)-const(100.0)/(const(1.0)+observable.rsi.Raw(observable.orderbook.MidPrice(book),timeframe,alpha))
}

package trash {
    package types {
        type T
        
        type R : trash.types.T
        
        type U : trash.types.T, trash.types.R
        
        type T1 = trash.types.T
    }
    
    package in1 {
        package in2 {
            def A(x : IFunction = constant(),
                  y : IObservable = if const(3.0)>x+const(2.0) then x else x*const(2.0)) : () => trash.types.T
                
        }
        
        def A(x : () => trash.types.T1 = trash.A()) : () => trash.types.U
            
    }
    
    def A(x : () => trash.types.T = trash.in1.in2.A()) : () => trash.types.R
        
}

type Side

type IOrderQueue

type IOrderBook

type IObservable : IFunction

type IFunction = () => Float

type ISingleAssetTrader

type IDifferentiable : IFunction

@python.function("Basic", "C=%(x)s")
def constant(x : Float = 1.0) : IFunction
     = const(x)

@python.intrinsic.function("Basic", "Null", "_constant._Null_Impl")
def null() : () => Float
    

@python.intrinsic.function("Basic", "C=%(x)s", "_constant._Constant_Impl")
def const(x : Float = 1.0) : IObservable
    

@python.intrinsic.function("Basic", "\\frac{d%(x)s}{dt}", "observable.derivative._Derivative_Impl")
def Derivative(x : IDifferentiable = observable.EW.Avg()) : () => Float
    

@python.observable("Basic", "If def(%(x)s) else %(elsePart)s")
def IfDefined(x : IFunction = constant(),
              elsePart : IFunction = constant()) : IFunction
     = if x<>null() then x else elsePart
