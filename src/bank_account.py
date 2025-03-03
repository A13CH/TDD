"""
Module 5 Assignment: bank_account.py
Author: Alec Hoelscher with help from Github Copilot
Date: 3/3/2024
Description: Implementation of a bank_account class in python which will be tested using pytest.
"""

class BankAccount:
    """A simple BankAccount class with methods to deposit, withdraw, and get_balance."""
    
    def __init__(self, account_number = 0, owner = "", balance = 0) -> None:
        """Initialize a BankAccount with an owner and an optional starting balance."""
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def from_json(self, data = []) -> None:
        """Deserialize a BankAccount object from a json file."""
        self.account_number = data['account_number']
        self.owner = data['owner']
        self.balance = data['balance']
        self.transactions = data['transactions']

    def to_json(self) -> dict:
        """Serialize a BankAccount object to a json file."""
        data = {
            'account_number': self.account_number,
            'owner': self.owner,
            'balance': self.balance,
            'transactions': self.transactions
        }
        return data

    def deposit(self, amount=0) -> None:
        """Deposit a positive amount to the account."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount=0) -> None:
        """Withdraw a positive amount if sufficient balance exists."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append(f"Withdrew {amount}")
            else:
                raise ValueError("Insufficient balance")
        else:
            raise ValueError("Withdrawal amount must be positive")
        
    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance
        
    def show_transactions(self) -> None:
        """Prints all account transactions."""
        for transaction in self.transactions:
            print(transaction)