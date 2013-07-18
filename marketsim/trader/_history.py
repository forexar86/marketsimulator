from marketsim import Event, _, Side
from collections import OrderedDict, defaultdict, namedtuple
from itertools import ifilter
from operator import attrgetter
from marketsim.order import Cancel

State = namedtuple('State', 'time price volume')

class TraderHistory(object):

    def __init__(self):
        self.matched = OrderedDict()
        self.pending = OrderedDict()
        self.cancelled = OrderedDict()
        self.amount = 0

    def bind(self, context):
        self._trader = context.trader
        self._scheduler = context.world

    def __call__(self, order):
        """ Track an order
        """
        if order.__class__.__name__ != 'Cancel' and not order.empty:
            order.on_matched += _(self).onMatched
            order.on_cancelled += _(self).onCancelled

            price = order.price if "price" in dir(order) else None
            # print self._trader._label, "send", order.side, order.volume, price
            self.pending[order] = [State(self.time, 0, order.volume)]

        return order

    @property
    def time(self):
        return self._scheduler.currentTime

    @property
    def lastMatched(self):
        if self.matched:
            return next(reversed(self.matched))
        else:
            return None

    def matchWithOwn(self, order):
        # TODO: Treat the case when an order might not be cancelled in time
        if order.__class__.__name__ != 'Cancel' and order.volume:
            side = order.side
            select = lambda x: x.side == side.opposite \
                and hasattr(x, "price") \
                and (not hasattr(order, "price") or side.better(order.price, x.price))
            orders = ifilter(select, self.pending)
            orders = sorted(orders, key=attrgetter('price'), reverse=(side == Side.Sell))

            for other in orders:
                if other.volume <= order.volume:
                    self._trader.send(Cancel(other))
                    order._volume -= other.volume
                elif order.volume > 0:
                    new = other.clone()
                    new._volume -= order.volume
                    self._trader.send(Cancel(other))
                    order = new

        return order

    @property
    def averagePrice(self):
        price = self.position_pnl / self.amount if self.amount else None
        return price

    def onMatched(self, order, other, (price, volume)):
        if volume <= 0:
            return

        self.pending[order].append(State(self.time, price, volume))

        previous = self.amount
        volume = volume if order.side == Side.Buy else -volume
        self.amount += volume
        # check if the position passed 0
        if previous*self.amount <= 0:
            self.position_pnl = self.amount*price
        else:
            self.position_pnl += volume*price

        if order.empty:
            self.matched[order] = self.pending.pop(order)

    def onCancelled(self, order):
        self.cancelled[order] = self.pending.pop(order)
        self.cancelled[order].append(State(self.time, 0, 0))