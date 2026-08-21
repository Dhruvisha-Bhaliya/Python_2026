#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:27:15 2026

@author: root
"""


from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, balance: float):
        self.balance = balance

    @abstractmethod
    def apply_interest(self):
        """Abstract method providing base interest logic for subclasses."""
        interest = self.balance * 0.05
        self.balance += interest
        print(
            f"[Account] Base interest (+5%): +${interest:.2f} | Balance:"
            f" ${self.balance:.2f}"
        )


class FeeAccount(Account):

    def apply_interest(self):
        super().apply_interest()
        fee = 15.0
        self.balance -= fee
        print(
            f"[FeeAccount] Maintenance fee: -${fee:.2f} | Balance:"
            f" ${self.balance:.2f}"
        )


class LoyaltyAccount(Account):

    def __init__(self, balance: float):
        super().__init__(balance)
        self.reward_points = 0

    def apply_interest(self):
        super().apply_interest()
        self.reward_points += 100
        print(
            "[LoyaltyAccount] Rewards added: +100 pts | Total:"
            f" {self.reward_points}"
        )


class PremiumCustomerAccount(LoyaltyAccount, FeeAccount):

    """Inherits from both LoyaltyAccount and FeeAccount."""

    pass


if __name__ == "__main__":
    try:
        base_acc = Account(1000.0)  
    except TypeError as e:
        print(f"Abstract Class Guard: {e}\n")

    acc = PremiumCustomerAccount(balance=1000.0)

    print("--- Method Execution Flow ---")
    acc.apply_interest()

    print("\n--- Method Resolution Order (MRO) ---")
    for cls in PremiumCustomerAccount.__mro__:
        print(cls.__name__)