from _base import *
from marketsim import combine, registry, bind, ops, meta, types
from marketsim.types import *

from marketsim.gen._intrinsic.order.limit import Order_Impl as Limit
from marketsim.gen._out.order._Limit import Limit as Factory
from marketsim.gen._out.order._curried._side_Limit import side_Limit as Side_Factory
from marketsim.gen._out.order._curried._volume_Limit import volume_Limit as Volume_Factory
from marketsim.gen._out.order._curried._price_Limit import price_Limit as Price_Factory
from marketsim.gen._out.order._curried._sideprice_Limit import sideprice_Limit as SidePrice_Factory
from marketsim.gen._out.order._curried._side_price_Limit import side_price_Limit as Side_Price_Factory
from marketsim.gen._out.order._curried._pricevolume_Limit import pricevolume_Limit as PriceVolume_Factory

Order = Limit

class LimitOrderFactory(types.IFunction[types.IOrder, types.SidePriceVolume]):
    
    def __call__(self, side, price, volume):
        return Order(side, price, volume)
    
@registry.expose(alias=['Limit'])
@sig(args=(Side,), rv=function((Price, Volume,), IOrder))
def LimitFactory(side):
    return bind.Construct(Order, side)

LimitFactory.__doc__ = Order.__doc__

class AdaptLimit_SidePriceBound(object):
    
    def __init__(self, orderFactory, side, price):
        self.orderFactory = orderFactory
        self.side = side
        self.price = price
        
    def __call__(self, volume):
        return self.orderFactory(self.side)(self.price, volume)

@registry.expose(alias=['Adapt limit order'])
class AdaptLimit(object):
    """ Adapts limit-like orders for usage where market-like orders are expected.
    User should provide *priceFunc* calculating price of order to create
    """
    
    def __init__(self, orderFactory = LimitFactory, priceFunc = ops.constant(100)):
        self.orderFactory = orderFactory
        self.priceFunc = priceFunc
        
    _properties = { 'orderFactory' : meta.function(args=(Side,), rv=function((Price, Volume,), IOrder)),
                    'priceFunc'    : meta.function((), Price)}
    
    _types = [meta.function(args=(Side,), rv=function((Volume,), IOrder))]
    
    def __repr__(self):
        return 'AdaptLimit(' + repr(self.orderFactory) + ', ' + repr(self.priceFunc) + ')'
        
    def __call__(self, side):
        price = self.priceFunc()
        price = self.priceFunc()
        return AdaptLimit_SidePriceBound(self.orderFactory, side, price)
