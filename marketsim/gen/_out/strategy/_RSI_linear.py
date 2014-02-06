from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "RSI_linear"])
class RSI_linear_Optional_________Float______IOrderGenerator___Optional__Float___Optional__IObservable__Float____Optional__Float_(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, orderFactory = None, alpha = None, k = None, timeframe = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._signedVolume_MarketSigned import signedVolume_MarketSigned as _order__curried_signedVolume_MarketSigned
        from marketsim import event
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_signedVolume_MarketSigned()
        self.alpha = alpha if alpha is not None else (1.0/14)
        self.k = k if k is not None else _const(-0.04)
        self.timeframe = timeframe if timeframe is not None else 1.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderFactory' : IFunction[IOrderGenerator,IFunction[float]],
        'alpha' : float,
        'k' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "RSI_linear(%(orderFactory)s, %(alpha)s, %(k)s, %(timeframe)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
        from marketsim.gen._out.strategy.position._RSI_linear import RSI_linear as _strategy_position_RSI_linear
        return _strategy_Generic(self.orderFactory(_strategy_position_RSI_linear(self.alpha,self.k,self.timeframe)))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def RSI_linear(orderFactory = None,alpha = None,k = None,timeframe = None): 
    return RSI_linear_Optional_________Float______IOrderGenerator___Optional__Float___Optional__IObservable__Float____Optional__Float_(orderFactory,alpha,k,timeframe)
