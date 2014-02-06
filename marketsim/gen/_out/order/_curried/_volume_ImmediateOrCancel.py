from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
@registry.expose(["Order", "ImmediateOrCancel"])
class volume_ImmediateOrCancel(IFunction[IOrderGenerator,IFunction[float]]):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._volume_Limit import volume_Limit as _order__curried_volume_Limit
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_volume_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._ImmediateOrCancel import ImmediateOrCancel
        volume = volume if volume is not None else _constant(1.0)
        proto = self.proto
        return ImmediateOrCancel(proto(volume))
    
