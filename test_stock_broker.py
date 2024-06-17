import io

from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import Mock, patch

from stock_broker_application import StockBrokerApplication

from stock_broker import KiwerStockBroker, NemoStockBroker
from stock_broker_application import StockBrokerApplication

NONAME_CODE = 12345

class TestStockBroker(TestCase):
    def test_same_instance(self):
        mk = Mock()
        app = StockBrokerApplication(mk)
        self.assertIs(app.get_broker(), mk)

    def test_login(self):
        ID = "D_Team"
        PSWD = "changeme"

        test_cases = [(KiwerStockBroker(), f"{ID} login success"),
                      (NemoStockBroker(), f"[NEMO]{ID} login GOOD"),
                      ]

        for stock_broker, login_message in test_cases:
            with self.subTest(f"{stock_broker.__class__.__name__} login Test!"):
                app = StockBrokerApplication(stock_broker)
                with io.StringIO() as buf, redirect_stdout(buf):
                    app.login(ID, PSWD)
                    captured_stdout = buf.getvalue().strip()
                    self.assertEqual(captured_stdout, login_message)

    def test_buy_mk(self):
        mk = Mock()
        app = StockBrokerApplication(mk)

        app.purchase(NONAME_CODE, 100, 10)
        mk.purchase.assert_called_once()

    @patch.object(StockBrokerApplication, 'get_price', return_value=5700)
    @patch.object(StockBrokerApplication, 'purchase')
    def test_buy_nice_timing(self, mock_purchase, mock_get_price):
        app = StockBrokerApplication(Mock())
        app.buy_nice_timing(NONAME_CODE, 11200, 5600)

        mock_get_price.assert_called_once_with(NONAME_CODE)
        mock_purchase.assert_called_once_with(NONAME_CODE, price=5700, amount=1)

    @patch.object(StockBrokerApplication, 'get_price', return_value=5400)
    @patch.object(StockBrokerApplication, 'sell')
    def test_sell_nice_timing(self, mock_sell, mock_get_price):
        app = StockBrokerApplication(Mock())
        app.sell_nice_timing(NONAME_CODE, amount=3, threshold=5500)

        mock_get_price.assert_called_once_with(NONAME_CODE)
        mock_sell.assert_called_once_with(NONAME_CODE, 5400, 3)
