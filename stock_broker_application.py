from typing import Optional

from stock_broker import StockBrokerInterface


class StockBrokerApplication:
    def __init__(self,
                 stock_broker: Optional[StockBrokerInterface] = None):
        self.__stock_broker: Optional[StockBrokerInterface] = stock_broker

    def set_stock_broker(self,
                         stock_broker: StockBrokerInterface) -> None:
        self.__stock_broker = stock_broker

    @property
    def broker(self) -> StockBrokerInterface:
        return self.__stock_broker

    def select_stock_brocker(self,
                             stock_broker: StockBrokerInterface) -> None:
        self.__stock_broker = stock_broker

    def login(self,
              _id: str,
              pw: str) -> None:
        self.__stock_broker.login(_id, pw)

    def purchase(self,
                 stock_code: str,
                 price: int,
                 amount: int) -> None:
        self.__stock_broker.purchase(stock_code, price, amount)

    def sell(self,
             stock_code: str,
             price: int,
             amount: int) -> None:
        self.__stock_broker.sell(stock_code, price, amount)

    def get_price(self,
                  stock_code: str) -> int:
        return self.__stock_broker.current_stock_price(stock_code)

    def buy_nice_timing(self,
                        stock_code: str,
                        price: int,
                        threshold: int) -> None:
        current_price = self.get_price(stock_code)
        if current_price > threshold:
            amount = price // current_price
            self.purchase(stock_code, price=current_price, amount=amount)

    def sell_nice_timing(self,
                         stock_code: str,
                         amount: int,
                         threshold: int) -> None:
        price = self.get_price(stock_code)
        if price < threshold:
            self.sell(stock_code, price, amount)
