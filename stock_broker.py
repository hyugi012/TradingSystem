from abc import ABC, abstractmethod

from overrides import overrides

from kiwer_api import KiwerAPI
from nemo_api import NemoAPI


class StockBrokerInterface(ABC):
    @abstractmethod
    def login(self,
              _id: str,
              pw: str) -> None:
        pass

    @abstractmethod
    def purchase(self,
                 stock_code: str,
                 price: int,
                 amount: int) -> None:
        pass

    @abstractmethod
    def sell(self,
             stock_code: str,
             price: int,
             amount: int) -> None:
        pass

    @abstractmethod
    def current_stock_price(self,
                            stock_code: str) -> int:
        pass


class NemoStockBroker(StockBrokerInterface):
    def __init__(self):
        super().__init__()
        self.__api = NemoAPI()

    @overrides
    def login(self,
              _id: str,
              pw: str) -> None:
        self.__api.cerification(_id, pw)

    @overrides
    def purchase(self,
                 stock_code: str,
                 price: int,
                 amount: int) -> None:
        self.__api.purchasing_stock(stock_code, price, amount)

    @overrides
    def sell(self,
             stock_code: str,
             price: int,
             amount: int) -> None:
        self.__api.selling_stock(stock_code, price, amount)

    @overrides
    def current_stock_price(self,
                            stock_code: str) -> int:
        return self.__api.get_market_price(stock_code, 0)


class KiwerStockBroker(StockBrokerInterface):
    def __init__(self):
        super().__init__()
        self.__api = KiwerAPI()

    @overrides
    def login(self,
              _id: str,
              pw: str) -> None:
        self.__api.login(_id, pw)

    @overrides
    def purchase(self,
                 stock_code: str,
                 price: int,
                 amount: int) -> None:
        self.__api.buy(stock_code, amount, price)

    @overrides
    def sell(self,
             stock_code: str,
             price: int,
             amount: int) -> None:
        self.__api.sell(stock_code, amount, price)

    @overrides
    def current_stock_price(self,
                            stock_code: str) -> int:
        return self.__api.current_price(stock_code)
