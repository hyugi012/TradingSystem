from unittest import TestCase
from unittest.mock import Mock, patch

from kiwer_api import KiwerAPI
from stock_broker import KiwerStockBroker
from stock_broker_application import StockBrokerApplication


class TestStockBroker(TestCase):
    def test_login(self):
        pass

    @patch.object(KiwerAPI, 'current_price', return_value=53000)
    def test_get_price(self, mock):
        ts = StockBrokerApplication(KiwerStockBroker())

        self.assertEqual(ts.get_price(123), 53000)
