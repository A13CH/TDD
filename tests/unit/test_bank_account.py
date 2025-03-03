import pytest
from src.bank_account import BankAccount

@pytest.fixture
def setup_account():
    return BankAccount(account_number="123456", owner="John Doe", balance=1000)

def test_deposit(setup_account):
    """Testing deposit function"""
    setup_account.deposit(1000)
    assert setup_account.get_balance() == 2000
    with pytest.raises(ValueError):
        setup_account.deposit(-100)
        setup_account.deposit(0)

def test_withdraw(setup_account):
    """Testing withdraw function"""
    setup_account.withdraw(500)
    assert setup_account.get_balance() == 500
    with pytest.raises(ValueError):
        setup_account.withdraw(10000)
        setup_account.withdraw(0)
        setup_account.withdraw(-100)

def test_getBalance(setup_account):
    """Testing the getBalance function"""
    assert setup_account.get_balance() == 1000
    setup_account.withdraw(500)
    assert setup_account.get_balance() == 500