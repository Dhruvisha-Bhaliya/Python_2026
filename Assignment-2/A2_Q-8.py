#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:24:06 2026

@author: root
"""

class Account:
    def __init__(self, balance: float):
        self.balance = balance

    def apply_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"[Account] Base interest (+5%): +${interest:.2f} | Balance: ${self.balance:.2f}")


class FeeAccount(Account):
    def apply_interest(self):
        super().apply_interest()
        fee = 15.0
        self.balance -= fee
        print(f"[FeeAccount] Maintenance fee: -${fee:.2f} | Balance: ${self.balance:.2f}")


class LoyaltyAccount(Account):
    def __init__(self, balance: float):
        super().__init__(balance)
        self.reward_points = 0

    def apply_interest(self):
        super().apply_interest()
        self.reward_points += 100
        print(f"[LoyaltyAccount] Rewards added: +100 pts | Total: {self.reward_points}")


class PremiumCustomerAccount(LoyaltyAccount, FeeAccount):
    """Inherits from both LoyaltyAccount and FeeAccount."""
    pass


if __name__ == "__main__":
    acc = PremiumCustomerAccount(balance=1000.0)

    print("--- Method Execution Flow ---")
    acc.apply_interest()

    print("\n--- Method Resolution Order (MRO) ---")
    for cls in PremiumCustomerAccount.__mro__:
        print(cls.__name__)