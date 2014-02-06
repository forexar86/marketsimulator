from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim.gen._intrinsic.observable.on_every_dt import _OnEveryDt_Impl
from marketsim import registry
from marketsim import float
@registry.expose(["Basic", "OnEveryDt"])
class OnEveryDt_Optional__Float___Optional__IFunction__Float__(Observable[float],_OnEveryDt_Impl):
    """ 
    """ 
    def __init__(self, dt = None, x = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        Observable[float].__init__(self)
        self.dt = dt if dt is not None else 1.0
        
        self.x = x if x is not None else _constant()
        
        rtti.check_fields(self)
        _OnEveryDt_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'dt' : float,
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "[%(x)s]_dt=%(dt)s" % self.__dict__
    
def OnEveryDt(dt = None,x = None): 
    return OnEveryDt_Optional__Float___Optional__IFunction__Float__(dt,x)
