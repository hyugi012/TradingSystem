import io

from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import Mock, patch

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


    def test_buy_mk(self):
        mk = Mock()
        app = StockBrokerApplication(mk)

        app.purchase('NONAME_CODE', 100, 10)
        mk.purchase.assert_called_once()

    def test_nemo_same_instance(self):
        nemo = NemoStockBroker()
        app = StockBrokerApplication(nemo)
        self.assertIs(app.get_broker(), nemo)
    @patch.object(NemoStockBroker, 'purchase')
    def test_nemo_buy(self, mock_purchase):
        nemo = NemoStockBroker()
        app = StockBrokerApplication(nemo)

        app.purchase('NONAME_CODE', 200, 15)
        mock_purchase.assert_called_once_with('NONAME_CODE', 200, 15)

    def test_nemo_same_instance(self):
        nemo = NemoStockBroker()
        app = StockBrokerApplication(nemo)
        self.assertIs(app.get_broker(), nemo)

    @patch.object(NemoStockBroker, 'purchase')
    def test_nemo_buy(self, mock_purchase):
        nemo = NemoStockBroker()
        app = StockBrokerApplication(nemo)

        app.purchase('NONAME_CODE', 200, 15)
        mock_purchase.assert_called_once_with('NONAME_CODE', 200, 15)

    def test_kiwer_same_instance(self):
        kiwer = KiwerStockBroker()
        app = StockBrokerApplication(kiwer)
        self.assertIs(app.get_broker(), kiwer)

    @patch.object(KiwerStockBroker, 'purchase')
    def test_nemo_buy(self, mock_purchase):
        kiwer = KiwerStockBroker()
        app = StockBrokerApplication(kiwer)

        app.purchase('NONAME_CODE', 50, 20)
        mock_purchase.assert_called_once_with('NONAME_CODE', 50, 20)



