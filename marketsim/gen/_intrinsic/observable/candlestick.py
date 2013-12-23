from marketsim import types, _, event, ops, context, CandleStick


from marketsim.gen._out.observable.Cumulative._Avg import Avg as CMA
from marketsim.gen._out.observable.Cumulative._StdDev import StdDev

class CandleSticks_Impl(ops.Observable[types.ICandleStick]):

    def __init__(self):
        ops.Observable[types.ICandleStick].__init__(self)
        self._event = event.subscribe(self.source, _(self)._update, self)
        event.subscribe(event.Every(ops.constant(self.timeframe)), _(self)._flush, self)
        self.reset()
        self._mean = CMA(self.source)
        self._stddev = StdDev(self.source)

    @property
    def attributes(self):
        return {}

    _internals = ["_mean", '_stddev']

    def reset(self):
        self._last = None
        self._open = None
        self._min = None
        self._max = None
        self._close = None

    def _flush(self, _):
        last = CandleStick(self._open, self._close,
                           self._min, self._max,
                           self._mean(), self._stddev()) \
                if self._open is not None else None
        self.reset()
        self._last = last
        self.fire(self)

    def _update(self, _):
        x = self.source()
        if x is not None:
            if self._open is None:
                self._open = x
                self._max = x
                self._min = x
                context.reset(self._mean)
                context.reset(self._stddev)
            if self._min > x: self._min = x
            if self._max < x: self._max = x
            self._close = x

    def __call__(self):
        return self._last