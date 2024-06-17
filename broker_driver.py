from abc import abstractmethod, ABC


class StockBroker(ABC):
    @abstractmethod
    def login(self, ID, PW):
        pass

    @abstractmethod
    def buy(self, code, price, num):
        pass

    @abstractmethod
    def sell(self, code, price, num):
        pass

    @abstractmethod
    def get_price(self, code):
        pass