from marketsim.ops._all import Observable
from marketsim import Volume
from marketsim import IOrderBook
from marketsim import registry
from marketsim import context
@registry.expose(["Asset", "LastTradeVolume"])
class LastTradeVolume_Optional__IOrderBook_(Observable[Volume]):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import Volume
        from marketsim import event
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        Observable[Volume].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "LastTradeVolume(Bid^{%(book)s})" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.orderbook._LastTradeVolume import LastTradeVolume as _orderbook_LastTradeVolume
        from marketsim.gen._out.orderbook._Bids import Bids as _orderbook_Bids
        return _orderbook_LastTradeVolume(_orderbook_Bids(self.book))
    
def LastTradeVolume(book = None): 
    return LastTradeVolume_Optional__IOrderBook_(book)
