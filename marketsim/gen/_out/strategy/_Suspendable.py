from marketsim.gen._intrinsic.strategy.suspendable import _Suspendable_Impl
from marketsim import IFunction
from marketsim import ISingleAssetStrategy
from marketsim import registry
from marketsim import bool
@registry.expose(["Strategy", "Suspendable"])
class Suspendable_Optional__ISingleAssetStrategy___Optional__IFunction__Boolean__(_Suspendable_Impl):
    """ 
    """ 
    def __init__(self, inner = None, predicate = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim.gen._out._true import true as _true
        from marketsim import rtti
        self.inner = inner if inner is not None else _strategy_Noise()
        self.predicate = predicate if predicate is not None else _true()
        rtti.check_fields(self)
        _Suspendable_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy,
        'predicate' : IFunction[bool]
    }
    def __repr__(self):
        return "Suspendable(%(inner)s, %(predicate)s)" % self.__dict__
    
def Suspendable(inner = None,predicate = None): 
    return Suspendable_Optional__ISingleAssetStrategy___Optional__IFunction__Boolean__(inner,predicate)
