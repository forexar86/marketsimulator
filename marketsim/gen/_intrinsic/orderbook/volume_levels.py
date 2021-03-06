from marketsim import event
from marketsim.gen._out.side._buy import Buy
from marketsim.gen._out.side._sell import Sell

from marketsim.gen._out._constant import constant

from marketsim.gen._out._intrinsic_base.orderbook.volume_levels import VolumeLevels_Base

class VolumeLevels_Impl(VolumeLevels_Base):

    def __init__(self):
        event.subscribe(event.Every(constant(1)), self.fire, self)

    @property
    def dataSource(self):
        return self

    @property
    def volumes(self):
        return [self.volumeDelta * i for i in range(self.volumeCount)]

    def __call__(self):
        queue = self.queue
        return [price for (volume, price) in queue.getVolumePrices(self.volumes)]

    @property
    def digits(self):
        return self.queue._digitsToShow

    @property
    def attributes(self):
        return {
            'smooth':True,
            'volumeLevels' : True,
            'fillBelow' : repr(self.queue.side) == "Buy",
            'fillAbove' : repr(self.queue.side) == "Sell"
        }