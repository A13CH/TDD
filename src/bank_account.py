"""
This module contains a class that represents a bank account.
The account supports deposit, withdraw, and get_balance operations.
Serialization and deserialization of the account is implemented using json.
"""

class BankAccount:
    """A simple BankAccount class with methods to deposit, withdraw, and get_balance."""
    
    def __init__(self, account_number, owner="", balance = 0):
        """Initialize a BankAccount with an owner and an optional starting balance."""
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def from_json(self) -> dict | None:
        """Deserialize a BankAccount object from a json file."""
        pass

    def to_json(self):
        """Serialize a BankAccount object to a json file."""
        pass

    def deposit(self, amount):
        """Deposit a positive amount to the account."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        """Withdraw a positive amount if sufficient balance exists."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append(f"Withdrew {amount}")
            else:
                raise ValueError("Insufficient balance")
        else:
            raise ValueError("Withdrawal amount must be positive")
        
    def get_balance(self):
        """Return the current balance."""
        return self.balance
        
    def show_transactions(self):
        """Prints all account transactions."""
        for transaction in self.transactions:
            print(transaction)