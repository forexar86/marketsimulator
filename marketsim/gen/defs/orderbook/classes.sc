@category = "Asset"
package orderbook
{
    /**
     * Order book for a single asset in a market.
     * Maintains two order queues for orders of different sides
     */
    @python.intrinsic("orderbook.local.Local_Impl")
    @label = "%(name)s"
    def Local(name          = "-orderbook-",
              tickSize      = 0.01,
              _digitsToShow = 2,
              timeseries    = [] : List[ITimeSerie]) : IOrderBook

    /**
     * Represent an *orderbook* from point of view of a remote trader connected
     * to the market by means of a *link* that introduces some latency in information propagation
     */
    @python.intrinsic("orderbook.remote.Remote_Impl")
    @label = "%(orderbook)s.name^remote"
    def Remote(orderbook     = Local(),
               link          = TwoWayLink(),
               timeseries    = [] : List[ITimeSerie]) : IOrderBook

    /**
     * Represents latency in information propagation from one agent to another one
     * (normally between a trader and a market).
     * Ensures that sending packets via a link preserves their order.
     */
    @python.intrinsic("orderbook.link.Link_Impl")
    def Link(/** function called for each packet in order to determine
               * when it will appear at the end point*/
             latency = const(0.001)) : ILink

    /**
     * Represents latency in information propagation between two agents
     * (normally between a trader and a market).
     * Ensures that sending packets via links preserves their order.
     * Holds two one-way links in opposite directions.
     */
    @python.intrinsic("orderbook.link.TwoWayLink_Impl")
    def TwoWayLink(/** Forward link (normally from a trader to a market)*/
                   up = Link(),
                   /** Backward link (normally from a market to a trader)*/
                   down = Link()) : ITwoWayLink

    /**
     *  Phantom orderbook used to refer to the order book associated with a single asset trader
     *
     *  May be used only in objects that are held by traders (so it is used in trader properties and strategies)
     */
    @python.intrinsic("orderbook.of_trader.OfTrader_Impl")
    @label = "N/A"
    @method = "Orderbook"
    def OfTrader(Trader = trader.SingleProxy() : IAccount) : IOrderBook

    /**
     *  Phantom orderbook that is used to refer to the current order book
     *
     *  May be used only in objects held by orderbooks (so it is normally used in orderbook properties)
     */
    @python.intrinsic("orderbook.of_trader.Proxy_Impl")
    @label = "N/A"
    def Proxy() : IOrderBook

    type IOrderQueueImpl

    @python.intrinsic("orderbook.queue.BestPrice_Impl")
    def BestPriceImpl(queue : IOrderQueueImpl) : IObservable[Price]

    @python.intrinsic("orderbook.queue.LastTrade_Impl")
    def LastTradeImpl() : Any

    @python.intrinsic("orderbook.local.Asks_Impl")
    @label = "N/A"
    def AsksImpl(tickSize : Float, book : IOrderBook) : IOrderQueueImpl

    @python.intrinsic("orderbook.local.Bids_Impl")
    @label = "N/A"
    def BidsImpl(tickSize : Float, book : IOrderBook) : IOrderQueueImpl

    @python.intrinsic("orderbook.remote.Queue_Impl")
    @label = "N/A"
    def RemoteQueueImpl(queue : IOrderQueueImpl, book : IOrderBook, link : ILink) : IOrderQueueImpl
}