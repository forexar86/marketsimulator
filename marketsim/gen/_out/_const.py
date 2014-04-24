# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservableint import IObservableint
from marketsim.gen._intrinsic._constant import Constant_Impl
@registry.expose(["Basic", "const"])
class const_Int(IObservableint,Constant_Impl):
    """ **Trivial observable always returning *x***
    
    
    Parameters are:
    
    **x**
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._iobservable._iobservableint import IObservableint
        from marketsim import rtti
        IObservableint.__init__(self)
        self.x = x if x is not None else 1
        rtti.check_fields(self)
        Constant_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : int
    }
    
    
    
    def __repr__(self):
        return "C=%(x)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        
        if hasattr(self, 'bind_impl'): self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic._constant import Constant_Impl
@registry.expose(["Basic", "const"])
class const_Float(IObservablefloat,Constant_Impl):
    """ **Trivial observable always returning *x***
    
    
    Parameters are:
    
    **x**
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
        from marketsim import rtti
        IObservablefloat.__init__(self)
        self.x = x if x is not None else 1.0
        rtti.check_fields(self)
        Constant_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : float
    }
    
    
    
    def __repr__(self):
        return "C=%(x)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        
        if hasattr(self, 'bind_impl'): self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def const(x = None): 
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, int):
        return const_Int(x)
    if x is None or rtti.can_be_casted(x, float):
        return const_Float(x)
    raise Exception('Cannot find suitable overload for const('+str(x) +':'+ str(type(x))+')')
