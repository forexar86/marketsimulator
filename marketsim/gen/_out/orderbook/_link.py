# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ilink import ILink
from marketsim.gen._intrinsic.orderbook.link import Link_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Asset", "Link"])
class Link_IObservableFloat(ILink,Link_Impl):
    """ **Represents latency in information propagation from one agent to another one**
    
     (normally between a trader and a market).
     Ensures that sending packets via a link preserves their order.
    
    Parameters are:
    
    **latency**
    	 function called for each packet in order to determine
    	 when it will appear at the end point
    """ 
    def __init__(self, latency = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        self.latency = latency if latency is not None else deref_opt(_const_Float(0.001))
        Link_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'latency' : IObservablefloat
    }
    
    
    def __repr__(self):
        return "Link(%(latency)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.latency.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.latency.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
        rtti.typecheck(IObservablefloat, self.latency)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.latency.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Link_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Link_Impl.reset(self)
    
def Link(latency = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if latency is None or rtti.can_be_casted(latency, IObservablefloat):
        return Link_IObservableFloat(latency)
    raise Exception('Cannot find suitable overload for Link('+str(latency) +':'+ str(type(latency))+')')
