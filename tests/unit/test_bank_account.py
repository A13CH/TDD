"""
Module 5 Assignment: test_bank_account.py
Author: Alec Hoelscher with help from Github Copilot
Date: 3/3/2024
Description: Implementation of unit tests for the bank_account class
"""

import pytest
from src.bank_account import BankAccount

@pytest.fixture
def setup_account() -> BankAccount:
    """Pytest fixture used to create a sample bank account for testing"""
    return BankAccount(account_number="123456", owner="John Doe", balance=1000)

@pytest.fixture
def setup_json() -> dict:
    """Pytest fixture used to create a sample json representation of a bank account for testing"""
    data = {
        'account_number': "123456",
        'owner': "John Doe",
        'balance': 1000,
        'transactions': []
    }
    return data

def test_deposit(setup_account) -> None:
    """Testing deposit function"""
    setup_account.deposit(1000)
    assert setup_account.get_balance() == 2000
    with pytest.raises(ValueError):
        setup_account.deposit(-100)
        setup_account.deposit(0)

def test_withdraw(setup_account) -> None:
    """Testing withdraw function"""
    setup_account.withdraw(500)
    assert setup_account.get_balance() == 500
    with pytest.raises(ValueError):
        setup_account.withdraw(10000)
        setup_account.withdraw(0)
        setup_account.withdraw(-100)

def test_getBalance(setup_account) -> None:
    """Testing the getBalance function"""
    assert setup_account.get_balance() == 1000
    setup_account.withdraw(500)
    assert setup_account.get_balance() == 500

def test_to_json(setup_account, setup_json) -> None:
    """Testing the to_json method"""
    setup_account.deposit(500)
    setup_json['balance'] = 1500
    setup_json['transactions'].append("Deposited 500")
    assert setup_account.to_json() == setup_json

def test_from_json(setup_account, setup_json) -> None:
    """Testing the from_json method"""
    setup_account.from_json(setup_json)
    assert setup_account.account_number == setup_json['account_number']
    assert setup_account.owner == setup_json['owner']
    assert setup_account.balance == setup_json['balance']
    assert setup_account.transactions == setup_json['transactions']