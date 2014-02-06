from marketsim import IFunction
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "Clamp0"])
class Clamp0_Optional__IFunction__Float__(Function[float]):
    """ 
    """ 
    def __init__(self, f = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.f = f if f is not None else _constant()
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunction[float]
    }
    def __repr__(self):
        return "Clamp0(%(f)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._Add import Add as _ops_Add
        from marketsim.gen._out.math._Max import Max as _math_Max
        from marketsim.gen._out._constant import constant as _constant
        return _ops_Add(_math_Max(_constant(0),self.f),_constant(1))
    
def Clamp0(f = None): 
    return Clamp0_Optional__IFunction__Float__(f)
