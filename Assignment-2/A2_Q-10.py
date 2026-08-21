#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:28:57 2026

@author: root
"""

from abc import ABC, abstractmethod


class InterestBearingInterface(ABC):

    @abstractmethod
    def interest_rate(self) -> float:
        """Returns the specific interest rate for the account."""
        pass

    @abstractmethod
    def apply_interest(self):
        """Calculates and applies interest to the balance."""
        pass


class Account(InterestBearingInterface):

    def __init__(self, balance: float):
        self.balance = balance

    def interest_rate(self) -> float:
        """Default base interest rate (5%)."""
        return 0.05

    def apply_interest(self):
        rate = self.interest_rate()
        interest = self.balance * rate
        self.balance += interest
        print(
            f"[Account] Applied {rate * 100:.1f}% interest:"
            f" +${interest:.2f} | Balance: ${self.balance:.2f}"
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

    def interest_rate(self) -> float:
        """Overrides interface method to offer premium 8% rate."""
        return 0.08


if __name__ == "__main__":
    acc = PremiumCustomerAccount(balance=1000.0)

    print("--- Interface Method Query ---")
    print(f"Current Interest Rate: {acc.interest_rate() * 100}%")

    print("\n--- Execution Flow via MRO ---")
    acc.apply_interest()