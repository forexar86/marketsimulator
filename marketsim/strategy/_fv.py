from marketsim import scheduler, observable, cached_property, types, Side

from _trend import SignalBase
from _wrap import wrapper

from marketsim.types import *

class FundamentalValueBase(SignalBase):

    def __init__(self, trader):
        SignalBase.__init__(self, trader)
        
    @property
    def _threshold(self):
        return 0.
    
    def _signalFunc(self):
        book = self._trader.book
        fv = self._fundamentalValue()
        
        # if current price is defined, compare it with the fundamental value and define the side
        return +1 if not book.asks.empty\
                  and book.asks.best.price < fv else\
               -1 if not book.bids.empty\
                  and book.bids.best.price > fv else\
               None

class _FundamentalValue_Impl(FundamentalValueBase):

    def __init__(self, trader, params):
        self._params = params
        self._orderFactoryT = params.orderFactory
        self._fundamentalValue = params.fundamentalValue  
        
        FundamentalValueBase.__init__(self, trader)
        
    def _volume(self, side):
        return self._params.volumeDistr()
        
    @cached_property
    def _eventGen(self):
        return scheduler.Timer(self._params.creationIntervalDistr)

from marketsim import order, mathutils
from marketsim.types import *

exec  wrapper("FundamentalValue", 
              [('orderFactory',         'order.Market.T',               'Side -> Volume -> Order'),
               ('fundamentalValue',     'mathutils.constant(100)',      '() -> Price'),
               ('volumeDistr',          'mathutils.rnd.expovariate(1.)','() -> Volume'),
               ('creationIntervalDistr','mathutils.rnd.expovariate(1.)','() -> TimeInterval')])


class _MeanReversion_Impl(FundamentalValueBase):

    def __init__(self,trader,params):

        self._orderFactoryT = params.orderFactory
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        avg = observable.Fold(observable.Price(trader.book), params.average)
        self._fundamentalValue = lambda: avg.value
        self._volume = lambda side: params.volumeDistr()  
        
        FundamentalValueBase.__init__(self, trader)

exec wrapper("MeanReversion",
             [('orderFactory',          'order.Market.T',                   'Side -> Volume -> Order'),
              ('average',               'mathutils.ewma(alpha = 0.15)',     'UpdatableValue'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',    '() -> Volume'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')])
        
class _Dependency_Impl(FundamentalValueBase):
    
    def __init__(self,trader,params):
        # start listening changes in a reference asset price
        self._params = params
        self._priceToDependOn = observable.Price(params.bookToDependOn) 
        self._orderFactoryT = params.orderFactory
        
        FundamentalValueBase.__init__(self, trader)

    def _fundamentalValue(self):
        return self._priceToDependOn.value * self._params.factor
    
    def _volume(self, side):
        oppositeQueue = self._trader.book.queue(side.opposite)
        # should we send limit and cancel orders here?
        oppositeVolume = oppositeQueue.volumeWithPriceBetterThan(self._fundamentalValue())
        # we want to trade orders only with a good price
        return min(oppositeVolume, self._params.volumeDistr())
    
    @property
    def _eventGen(self):
        return self._priceToDependOn        

exec wrapper("Dependency", 
             [('bookToDependOn','None',                         'OrderBook'),
              ('orderFactory',  'order.Market.T',               'Side -> Volume -> Order'),
              ('factor',        '1.',                           'positive'),
              ('volumeDistr',   'mathutils.rnd.expovariate(.1)','() -> Volume')])