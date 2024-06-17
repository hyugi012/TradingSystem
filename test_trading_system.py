from unittest import TestCase
from unittest.mock import Mock

from trading_system import TradingSystem


class TestTradingSystem(TestCase):
    def setUp(self):
        super().setUp()
        mk = Mock()
        self.ts = TradingSystem(mk)

    def test_select_stock_broker(self):
        pass

    def test_login(self):
        ID = ""
        PW = ""
        ret = self.ts.login(ID, PW)
        self.assertTrue(ret)

    def test_buy(self):
        code = ""
        price = 0
        num = 0
        ret = self.ts.buy(code, price, num)
        self.assertTrue(ret)

    def test_sell(self):
        code = ""
        price = 0
        num = 0
        ret = self.ts.sell(code, price, num)
        self.assertTrue(ret)

    def test_get_price(self):
        code = ""
        ret = self.ts.get_price(code)
        self.assertEqual(ret, 0)

    def test_buy_nice_timing(self):
        pass

    def test_sell_nice_timing(self):
        pass
