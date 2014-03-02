from marketsim import registry
from marketsim.gen._out.strategy._marketmaker import MarketMaker
@registry.expose(["-", "Delta"])
class Delta_strategyMarketMaker(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy._marketmaker import MarketMaker_FloatFloat as _strategy_MarketMaker_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_MarketMaker_FloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketMaker
    }
    def __repr__(self):
        return "Delta(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.delta
    
from marketsim import registry
from marketsim.gen._out.strategy._marketdata import MarketData
@registry.expose(["-", "Delta"])
class Delta_strategyMarketData(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy._marketdata import MarketData_StringStringStringFloatFloat as _strategy_MarketData_StringStringStringFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_MarketData_StringStringStringFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketData
    }
    def __repr__(self):
        return "Delta(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.delta
    
def Delta(x = None): 
    from marketsim.gen._out.strategy._marketmaker import MarketMaker
    from marketsim.gen._out.strategy._marketdata import MarketData
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MarketMaker):
        return Delta_strategyMarketMaker(x)
    if x is None or rtti.can_be_casted(x, MarketData):
        return Delta_strategyMarketData(x)
    raise Exception('Cannot find suitable overload for Delta('+str(x) +':'+ str(type(x))+')')