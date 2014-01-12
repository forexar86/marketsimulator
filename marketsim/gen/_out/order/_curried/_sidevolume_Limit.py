from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "Limit"])
class sidevolume_Limit(IFunction[IOrderGenerator, IFunction[Side],IFunction[float]

]):
    """ 
    """ 
    def __init__(self, price = None):
        from marketsim.gen._out._constant import constant as _constant
        self.price = price if price is not None else _constant(100.0)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'price' : IFunction[float]
    }
    def __repr__(self):
        return "sidevolume_Limit(%(price)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._Limit import Limit
        side = side if side is not None else _side_Sell()
        volume = volume if volume is not None else _constant(1.0)
        price = self.price
        return Limit(side, price, volume)
    