from unittest import TestCase
from unittest.mock import Mock

from stock_broker import KiwerStockBroker, NemoStockBroker
from stock_broker_application import StockBrokerApplication


class TestStockBroker(TestCase):

    def sell_mock_function(self, stock_code, price, amount):
        print(stock_code + ' : Sell stock ( ' + str(price) + ' * ' + str(amount))

    def test_login(self):
        pass

    def test_sell_broker(self):
        broker_mock = Mock()
        broker_mock.sell.side_effect = self.sell_mock_function
        sut = StockBrokerApplication(broker_mock)

        sut.sell(123, 10000, 456)

        broker_mock.sell.assert_called_once()
