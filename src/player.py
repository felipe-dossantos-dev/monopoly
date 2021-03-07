import random
import uuid
from src.estate import Estate


class ImpulsiveStrategy:
    def should_buy(self, balance: int, estate: Estate):
        return True


class PickyStrategy:
    def __init__(self, min_rent_value=50) -> None:
        self.min_rent_value = min_rent_value

    def should_buy(self, balance: int, estate: Estate):
        return estate.rent_value > self.min_rent_value


class CautiosStrategy:
    def __init__(self, min_balance_after_buy=80) -> None:
        self.min_balance_after_buy = min_balance_after_buy

    def should_buy(self, balance: int, estate: Estate):
        return balance - estate.buy_cost > self.min_balance_after_buy


class RandomStrategy:
    def should_buy(self, balance: int, estate: Estate):
        return random.choice([True, False])


class Player:
    def __init__(self, strategy, balance=300) -> None:
        self.initial_balance = balance
        self.balance = balance
        self.strategy = strategy
        self.id = uuid.uuid4()

    def play_dice(self):
        return random.choice([1, 2, 3, 4, 5, 6])

    def should_buy(self, estate: Estate):
        return self.balance >= estate.buy_cost and self.strategy.should_buy(
            self.balance, estate
        )

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value

    def buy(self, estate: Estate):
        self.withdraw(estate.buy_cost)
        estate.set_owner(self)

    def pay_rent(self, estate: Estate):
        self.withdraw(estate.rent_value)
        estate.pay_rent()

    def is_broken(self):
        return self.balance < 0

    def reset(self):
        self.balance = self.initial_balance

    def __hash__(self):
        return self.id.__hash__()

    def __eq__(self, other):
        return self.id.__eq__(other)

    def __repr__(self) -> str:
        return f"Player[{self.id}] with strategy {type(self.strategy)}"
