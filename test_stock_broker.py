import io

from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import patch, Mock

from stock_broker import KiwerStockBroker, NemoStockBroker, StockBrokerInterface
from stock_broker_application import StockBrokerApplication


class TestStockBroker(TestCase):
    def setUp(self):
        self.__app = StockBrokerApplication()
        self.__brokers = {
            "NEMO": NemoStockBroker(),
            "KIWER": KiwerStockBroker()
        }

    @patch.object(KiwerStockBroker, 'current_stock_price', return_value=53000)
    def test_get_price_for_kiwer(self, mock):
        ts = StockBrokerApplication(KiwerStockBroker())

        self.assertEqual(ts.get_price(123), 53000)

    @patch.object(NemoStockBroker, 'current_stock_price', return_value=52000)
    def test_get_price_for_nemo(self, mock):
        ts = StockBrokerApplication(NemoStockBroker())

        self.assertEqual(ts.get_price(123), 52000)

    def test_login(self):
        _id = "D_TEAM"
        pw = "changeme"

        expected_outputs = {
            "NEMO": f"[NEMO]{_id} login GOOD",
            "KIWER": f"{_id} login success"
        }

        for key, broker in self.__brokers.items():
            with (self.subTest(f"{key} broker login test!"),
                  io.StringIO() as buf, redirect_stdout(buf)):
                self.__app.set_stock_broker(broker)
                self.__app.login(_id, pw)
                self.assertEqual(expected_outputs[key], buf.getvalue().strip())

    def test_buy(self):
        stock_code = "TEST"
        price = 1530
        amount = 30

        expected_outputs = {
            "NEMO": f"[NEMO]{stock_code} buy stock ( price : {price} ) * ( count : {amount})",
            "KIWER": f"{stock_code} : Buy stock ( {price} * {amount}"
        }

        for key, broker in self.__brokers.items():
            with (self.subTest(f"{key} broker buy test!"),
                  io.StringIO() as buf, redirect_stdout(buf)):
                self.__app.set_stock_broker(broker)
                self.__app.purchase(stock_code, price, amount)
                self.assertEqual(expected_outputs[key], buf.getvalue().strip())

    def test_sell(self):
        stock_code = "TEST"
        price = 1530
        amount = 30

        expected_outputs = {
            "NEMO": f"[NEMO]{stock_code} sell stock ( price : {price} ) * ( count : {amount})",
            "KIWER": f"{stock_code} : Sell stock ( {price} * {amount}"
        }

        for key, broker in self.__brokers.items():
            with (self.subTest(f"{key} broker sell test!"),
                  io.StringIO() as buf, redirect_stdout(buf)):
                self.__app.set_stock_broker(broker)
                self.__app.sell(stock_code, price, amount)
                self.assertEqual(expected_outputs[key], buf.getvalue().strip())

    def test_set_stock_brocker(self):
        mock_broker: StockBrokerInterface = Mock(spec=StockBrokerInterface)
        self.__app.set_stock_broker(mock_broker)

        for key, broker in self.__brokers.items():
            with self.subTest(f"{key} broker set test!"):
                self.__app.set_stock_broker(broker)
                self.assertEqual(broker, self.__app.broker)
