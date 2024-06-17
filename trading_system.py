from broker_driver import StockBroker


class TradingSystem:
    def __init__(self, api: StockBroker):
        self.api = api

    def login(self, ID, PW):
        pass

    def buy(self, code, price, num):
        pass

    def sell(self, code, price, num):
        pass

    def get_price(self, code):
        pass