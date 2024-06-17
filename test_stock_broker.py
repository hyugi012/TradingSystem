from unittest import TestCase
from unittest.mock import Mock, patch

from stock_broker_application import StockBrokerApplication


class TestStockBroker(TestCase):
    def test_login(self):
        pass

    def test_get_price(self):
        mk = Mock()
        ts = StockBrokerApplication(mk)
        mk.current_stock_price.return_value = 53000

        self.assertEqual(ts.get_price(123), 53000)
