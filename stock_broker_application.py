from stock_broker import StockBrokerInterface


class StockBrokerApplication:
    def __init__(self,
                 stock_broker: StockBrokerInterface):
        self.__stock_broker: StockBrokerInterface = stock_broker

    def get_broker(self):
        return self.__stock_broker

    def login(self,
              _id: str,
              pw: str) -> None:
        self.__stock_broker.login(_id, pw)

    def purchase(self,
                 stock_code: int,
                 price: int,
                 amount: int) -> None:
        self.__stock_broker.purchase(stock_code, price, amount)

    def sell(self,
             stock_code: int,
             price: int,
             amount: int) -> None:
        self.__stock_broker.sell(stock_code, price, amount)

    def get_price(self,
                  stock_code: int) -> int:
        return self.__stock_broker.current_stock_price(stock_code)

    def buy_nice_timing(self):
        pass

    def sell_nice_timing(self):
        pass
