import pytest
from account import *


class Test:
    def setup_method(self):
        self.test_account = Account('John')

    def teardown_method(self):
        del self.test_account

    def test_init(self):
        assert self.test_account.get_name() == 'John'
        assert self.test_account.get_balance() == 0

    def test_deposit(self):
        assert self.test_account.deposit(0) is False
        assert self.test_account.get_balance() == pytest.approx(0, abs=0.001)
        assert self.test_account.deposit(-38) is False
        assert self.test_account.get_balance() == pytest.approx(0, abs=0.001)
        assert self.test_account.deposit(5) is True
        assert self.test_account.get_balance() == pytest.approx(5, abs=0.001)
        assert self.test_account.deposit(10.38) is True
        assert self.test_account.get_balance() == pytest.approx(15.38, abs=0.001)

    def test_withdraw(self):
        self.test_account.deposit(50)
        assert self.test_account.withdraw(0) is False
        assert self.test_account.get_balance() == pytest.approx(50, abs=0.001)
        assert self.test_account.withdraw(-92) is False
        assert self.test_account.get_balance() == pytest.approx(50, abs=0.001)
        assert self.test_account.withdraw(65) is False
        assert self.test_account.get_balance() == pytest.approx(50, abs=0.001)
        assert self.test_account.withdraw(45) is True
        assert self.test_account.get_balance() == pytest.approx(5, abs=0.001)
        assert self.test_account.withdraw(4.98) is True
        assert self.test_account.get_balance() == pytest.approx(0.02, abs=0.001)
