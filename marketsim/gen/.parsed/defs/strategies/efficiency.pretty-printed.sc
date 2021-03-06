
package strategy.account() {
    // defined at defs\strategies\efficiency.sc: 3.5
    /** Associated with a strategy account that tracks
     *  how orders sent by the strategy have been actually traded
     */
    @python.intrinsic("strategy.account.Account_Impl")
    @curried("inner")
    def Real(/** strategy to track */ inner : Optional[ISingleAssetStrategy] = Empty()) : IAccount
    
    // defined at defs\strategies\efficiency.sc: 12.5
    /** Associated with a strategy account that evaluates for every order sent by the strategy
     *  how it would be traded by sending request.evalMarketOrder
     *  (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
     *  but we want evaluate in any case would it be profitable or not)
     */
    @python.intrinsic("strategy.account.VirtualMarket_Impl")
    @curried("inner")
    def VirtualMarket(/** strategy to track */ inner : Optional[ISingleAssetStrategy] = Empty()) : IAccount
    
    def real = inner.inner_Real
    
    def virtualMarket = inner.inner_VirtualMarket
}

package strategy.weight() {
    def atanPow = f.f_AtanPow
    
    def clamp0 = f.f_Clamp0
    
    def identityF = f.f_IdentityF
    
    def score = trader.trader_Score
    
    def unit = trader.trader_Unit
    
    def efficiency = trader.trader_TraderEfficiency
    
    def efficiencyTrend = trader.trader_TraderEfficiencyTrend
    
    def chooseTheBest = array.array_ChooseTheBest
    
    def identityL = array.array_IdentityL
    
    // defined at defs\strategies\efficiency.sc: 54.5
    /** scaling function = atan(base^f(x))
     */
    @curried("f")
    def AtanPow(/** function to scale */ f : Optional[IFunction[Float]] = constant(1.0),
                /** base for power function */ base = 1.002) : IFunction[Float] = const(base)~>Pow(f)~>Atan
    
    // defined at defs\strategies\efficiency.sc: 66.5
    /** scaling function = max(0, f(x)) + 1
     */
    @curried("f")
    def Clamp0(/** function to scale */ f : Optional[IFunction[Float]] = constant(1.0)) : IFunction[Float] = math.Max(0,f)+1
    
    // defined at defs\strategies\efficiency.sc: 75.5
    /** identity scaling = f(x)
     */
    @curried("f")
    def IdentityF(f : Optional[IFunction[Float]] = constant(1.0)) : IFunction[Float] = f
    
    // defined at defs\strategies\efficiency.sc: 80.5
    /** Calculates how many times efficiency of trader went up and went down
     * Returns difference between them.
     *
     * TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
     */
    @python.intrinsic("strategy.weight.Score_Impl")
    @curried("trader")
    def Score(/** account in question */ trader : IAccount = trader.SingleProxy()) : IFunction[Float]
    
    // defined at defs\strategies\efficiency.sc: 90.5
    /** Unit function. Used to simulate uniform random choice of a strategy
     */
    @curried("trader")
    def Unit(/** account in question */ trader : IAccount = trader.SingleProxy()) : IFunction[Float] = constant(1.0)
    
    // defined at defs\strategies\efficiency.sc: 99.5
    /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
     */
    @curried("trader")
    def TraderEfficiency(/** account in question */ trader : IAccount = trader.SingleProxy()) : IFunction[Float] = trader~>Efficiency
    
    // defined at defs\strategies\efficiency.sc: 108.5
    /** Returns first derivative of a moving average of the trader efficiency
     */
    @curried("trader")
    def TraderEfficiencyTrend(/** account in question */ trader : IAccount = trader.SingleProxy(),
                              /** parameter alpha for the moving average */ alpha = 0.15) : IFunction[Float] = trader~>EfficiencyTrend(alpha)
    
    // defined at defs\strategies\efficiency.sc: 120.5
    /** Identity function for an array of floats
     */
    @python.intrinsic("strategy.weight.Identity_Impl")
    @curried("array")
    def IdentityL(array : Optional[List[Float]] = []) : IFunction[List[Float]]
    
    // defined at defs\strategies\efficiency.sc: 127.5
    /** Function returning an array of length *len(array)*
     *  having 1 at the index of the maximal element and 0 are at the rest
     */
    @python.intrinsic("strategy.weight.ChooseTheBest_Impl")
    @curried("array")
    def ChooseTheBest(array : Optional[List[Float]] = []) : IFunction[List[Float]]
}
