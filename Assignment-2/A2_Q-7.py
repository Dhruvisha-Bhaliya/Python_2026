#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:23:13 2026

@author: root
"""

class BankAccount:
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = initial_balance  
        self.is_active = True
        print(f"Account '{self.account_number}' created for {self.holder_name}.")

    def deposit(self, amount: float):
        """Adds money to the account balance."""
        if not self.is_active:
            print("Error: Account is closed.")
            return
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f} | New Balance: ${self.__balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount: float):
        """Debits money from the account balance."""
        if not self.is_active:
            print("Error: Account is closed.")
            return
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f} | Remaining Balance: ${self.__balance:.2f}")
        else:
            print("Transaction failed: Insufficient funds or invalid amount.")

    def get_balance(self):
        """Getter method to safely access private __balance."""
        if self.is_active:
            return self.__balance
        return 0.0

    def delete_account(self):
        """Deletes/Closes the account."""
        if self.is_active:
            self.is_active = False
            self.__balance = 0.0
            print(f"Account '{self.account_number}' has been deleted.")
        else:
            print("Account is already closed.")


class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0, interest_rate: float = 0.05):
        # Call parent class constructor
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Calculates and deposits earned interest."""
        if self.is_active:
            earned = self.get_balance() * self.interest_rate
            print(f"Applying {self.interest_rate * 100}% interest (${earned:.2f})...")
            self.deposit(earned)


if __name__ == "__main__":
    print("=== 1. Create Account ===")
    acc = SavingsAccount(account_number="SA-101", holder_name="Rahul", initial_balance=1000.0)

    print("\n=== 2. Encapsulation Check ===")
    print(f"Balance accessed via Getter: ${acc.get_balance():.2f}")

    print("\n=== 3. Deposit & Withdraw ===")
    acc.deposit(500.0)
    acc.withdraw(200.0)

    print("\n=== 4. Inheritance Feature (Apply Interest) ===")
    acc.apply_interest()

    print("\n=== 5. Delete Account ===")
    acc.delete_account()
    acc.deposit(100.0)