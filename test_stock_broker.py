import io

from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import Mock

from stock_broker import KiwerStockBroker, NemoStockBroker
from stock_broker_application import StockBrokerApplication


class TestStockBroker(TestCase):
    def sell_mock_function(self, stock_code, price, amount):
        print('[Mock]' + stock_code + ' : Sell stock ( ' + str(price) + ' * ' + str(amount) + ' )')

    def sell_test_function(self, broker):
        sut = StockBrokerApplication(broker)

        sut.sell(123, 10000, 456)

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
        
    def test_sell_with_mock_broker(self):
        broker_mock = Mock()
        broker_mock.sell.side_effect = self.sell_mock_function

        self.sell_test_function(broker_mock)

        broker_mock.sell.assert_called_once()

    def test_sell_with_specific_broker(self):
        for broker in [NemoStockBroker(), KiwerStockBroker()]:
            with self.subTest(f'Broker: {broker.__class__.__name__}'):
                self.sell_test_function(broker)
