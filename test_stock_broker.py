import io

from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import Mock

from stock_broker_application import StockBrokerApplication

from stock_broker import KiwerStockBroker, NemoStockBroker
from stock_broker_application import StockBrokerApplication


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

    def test_select_stock_brocker(self):
        test_cases = [(KiwerStockBroker(), NemoStockBroker()),
                      (NemoStockBroker(), KiwerStockBroker()),
                      ]
        for base_broker, changed_broker in test_cases:
            with self.subTest(f"{base_broker.__class__.__name__} change to {changed_broker.__class__.__name__} Test!"):
                app = StockBrokerApplication(base_broker)
                app.select_stock_brocker(changed_broker)
                self.assertIs(app.get_broker(), changed_broker)

    def test_buy_mk(self):
        mk = Mock()
        app = StockBrokerApplication(mk)

        app.purchase('NONAME_CODE', 100, 10)
        mk.purchase.assert_called_once()

