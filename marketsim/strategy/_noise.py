from marketsim import scheduler, order, _, mathutils, types, registry, ops, meta, observable
from _basic import Strategy
from _two_sides import TwoSides
from _periodic import Periodic, Generic
from _wrap import wrapper2
from marketsim.types import *

class _Noise_Impl(TwoSides):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        TwoSides.__init__(self)
        
    def _orderFunc(self):
        conv = types.Side.byId
        return (types.Side.byId(self.sideDistr()), (int(self.volumeDistr()),)) 

exec wrapper2("Noise", 
             """ Noise strategy is a quite dummy strategy that randomly creates an order 
                 and sends it to the order book. 
                 
                 It has following parameters:

                 |orderFactoryT| 
                     order factory function (default: order.Market.T)

                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                     
                 |sideDistr| 
                     side of orders to create 
                     (default: discrete uniform distribution P(Sell)=P(Buy)=.5)
             """,
             [("orderFactory",          "order.MarketFactory",          'Side -> Volume -> IOrder'),
              ("sideDistr",             "mathutils.rnd.randint(0,1)",   "() -> int"), # in fact it should be () -> Side
              ("volumeDistr",           "mathutils.rnd.expovariate(1.)",'() -> Volume'),
              ("creationIntervalDistr", "mathutils.rnd.expovariate(1.)",'() -> TimeInterval')])

import _wrap

class NoiseEx(types.ISingleAssetStrategy):
    
    def getImpl(self):
        return Periodic(orderFactory = self.orderFactory, 
                        eventGen     = scheduler.Timer(self.creationIntervalDistr), 
                        sideFunc     = observable.side.Random(), 
                        volumeFunc   = self.volumeDistr)
        
_wrap.strategy(NoiseEx, ['Periodic', 'Noise'], 
                 """ Noise strategy is a quite dummy strategy that randomly creates an order 
                     and sends it to the order book. 
                     
                     It has following parameters:
    
                     |orderFactory| 
                         order factory function (default: order.Market.T)
    
                     |creationIntervalDistr| 
                         defines intervals of time between order creation 
                         (default: exponential distribution with |lambda| = 1)
                         
                     |volumeDistr| 
                         defines volumes of orders to create 
                         (default: exponential distribution with |lambda| = 1)
                 """,
                 [
                  ("orderFactory",          "order.MarketFactory",          'Side -> Volume -> IOrder'),
                  ("volumeDistr",           "mathutils.rnd.expovariate(1.)",'() -> Volume'),
                  ("creationIntervalDistr", "mathutils.rnd.expovariate(1.)",'() -> TimeInterval')
                 ], globals())

class Noise2Ex(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        return { 'side' : observable.side.Random() }
    
    def getImpl(self):
        return Generic(eventGen = scheduler.Timer(self.creationIntervalDistr), 
                       orderFactory = self.orderFactory(_.side))
        
_wrap.strategy(Noise2Ex, ['Periodic', 'Noise2'], 
                 """ Noise strategy is a quite dummy strategy that randomly creates an order 
                     and sends it to the order book. 
                     
                     It has following parameters:
    
                     |orderFactory| 
                         order factory function (default: order.Market.T)
    
                     |creationIntervalDistr| 
                         defines intervals of time between order creation 
                         (default: exponential distribution with |lambda| = 1)
                 """,
                 [
                  ("orderFactory",          "order.factory.Side_Market()",  'ISide_IOrderGenerator'),
                  ("creationIntervalDistr", "mathutils.rnd.expovariate(1.)",'() -> TimeInterval')
                 ], globals())
