# generated with class generator.python.curried$after_typing$Curried
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat import IFunctionIFunctionfloat_from_IFunctionfloat
@registry.expose(["Strategy", "f_AtanPow"])
class f_AtanPow_Float(IFunctionIFunctionfloat_from_IFunctionfloat):
    """ **scaling function = atan(base^f(x))**
    
    
    Parameters are:
    
    **base**
    	 base for power function 
    """ 
    def __init__(self, base = None):
        self.base = base if base is not None else 1.002
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'base' : float
    }
    
    
    def __repr__(self):
        return "f_AtanPow(%(base)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        rtti.typecheck(float, self.base)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, f = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.weight._atanpow import AtanPow_FloatFloat as _strategy_weight_AtanPow_FloatFloat
        f = f if f is not None else deref_opt(_constant_Float(1.0))
        base = self.base
        return _strategy_weight_AtanPow_FloatFloat(f,base)
    
def f_AtanPow(base = None): 
    from marketsim import rtti
    if base is None or rtti.can_be_casted(base, float):
        return f_AtanPow_Float(base)
    raise Exception('Cannot find suitable overload for f_AtanPow('+str(base) +':'+ str(type(base))+')')
