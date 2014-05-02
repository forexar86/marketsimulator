# generated with class generator.python.random$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "lognormvariate"])
class lognormvariate_FloatFloat(IFunctionfloat):
    """ **Log normal distribution**
    
    
     If you take the natural logarithm of this distribution,
      you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
      |mu| can have any value, and |sigma| must be greater than zero.
    
    Parameters are:
    
    **Mu**
    
    **Sigma**
    """ 
    def __init__(self, Mu = None, Sigma = None):
        self.Mu = Mu if Mu is not None else 0.0
        self.Sigma = Sigma if Sigma is not None else 1.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Mu' : float,
        'Sigma' : float
    }
    
    
    
    
    def __repr__(self):
        return "lognormvariate(%(Mu)s, %(Sigma)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        rtti.typecheck(float, self.Mu)
        rtti.typecheck(float, self.Sigma)
    
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
    
    def __call__(self, *args, **kwargs):
        import random
        return random.lognormvariate(self.Mu, self.Sigma)
    
    def _casts_to(self, dst):
        return lognormvariate_FloatFloat._types[0]._casts_to(dst)
    
def lognormvariate(Mu = None,Sigma = None): 
    from marketsim import rtti
    if Mu is None or rtti.can_be_casted(Mu, float):
        if Sigma is None or rtti.can_be_casted(Sigma, float):
            return lognormvariate_FloatFloat(Mu,Sigma)
    raise Exception('Cannot find suitable overload for lognormvariate('+str(Mu) +':'+ str(type(Mu))+','+str(Sigma) +':'+ str(type(Sigma))+')')
