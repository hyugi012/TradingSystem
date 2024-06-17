from unittest import TestCase
from unittest.mock import Mock

from stock_broker_application import StockBrokerApplication


class TestStockBroker(TestCase):
    def test_same_instance(self):
        mk = Mock()
        app = StockBrokerApplication(mk)
        self.assertIs(app.get_broker(), mk)

    def test_login(self):
        pass

    def test_buy_mk(self):
        mk = Mock()
        app = StockBrokerApplication(mk)

        app.purchase('NONAME_CODE', 100, 10)
        mk.purchase.assert_called_once()




