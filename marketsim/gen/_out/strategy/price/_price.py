# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
@registry.expose(["Price function", "Price"])
class Price_strategypriceLiquidityProviderSide(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider_FloatFloatIOrderBook as _strategy_price_LiquidityProvider_FloatFloatIOrderBook
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_price_LiquidityProvider_FloatFloatIOrderBook())
        self.side = side if side is not None else deref_opt(_side_Sell_())
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : LiquidityProvider,
        'side' : IFunctionSide
    }
    
    
    
    
    def __repr__(self):
        return "Price(%(x)s, %(side)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        self.side.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        self.side.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
        from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
        rtti.typecheck(LiquidityProvider, self.x)
        rtti.typecheck(IFunctionSide, self.side)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        self.side.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.strategy.price._pricedistr import PriceDistr_strategypriceLiquidityProvider as _strategy_price_PriceDistr_strategypriceLiquidityProvider
        from marketsim.gen._out.strategy.price._book import Book_strategypriceLiquidityProvider as _strategy_price_Book_strategypriceLiquidityProvider
        from marketsim.gen._out.orderbook._queue import Queue_IOrderBookSide as _orderbook_Queue_IOrderBookSide
        from marketsim.gen._out.strategy.price._initialvalue import InitialValue_strategypriceLiquidityProvider as _strategy_price_InitialValue_strategypriceLiquidityProvider
        from marketsim.gen._out.orderbook._safesideprice import SafeSidePrice_IOrderQueueFloat as _orderbook_SafeSidePrice_IOrderQueueFloat
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatFloat as _ops_Mul_IObservableFloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        return deref_opt(_ops_Mul_IObservableFloatFloat(deref_opt(_orderbook_SafeSidePrice_IOrderQueueFloat(deref_opt(_orderbook_Queue_IOrderBookSide(deref_opt(_strategy_price_Book_strategypriceLiquidityProvider(self.x)),self.side)),deref_opt(_constant_Float(deref_opt(_strategy_price_InitialValue_strategypriceLiquidityProvider(self.x)))))),deref_opt(_strategy_price_PriceDistr_strategypriceLiquidityProvider(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Price(x = None,side = None): 
    from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, LiquidityProvider):
        if side is None or rtti.can_be_casted(side, IFunctionSide):
            return Price_strategypriceLiquidityProviderSide(x,side)
    raise Exception('Cannot find suitable overload for Price('+str(x) +':'+ str(type(x))+','+str(side) +':'+ str(type(side))+')')
