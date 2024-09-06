import pytest

from money.money import Money
from money.money_adder import MoneyAdder


class TestMoney:
    adder = MoneyAdder()

    def test_2and4_equal6(self):
        money1 = Money(4)
        money2 = Money(2)

        money_sum = self.adder.add(money1, money2)
        assert money_sum.amount == 6

    def test_3and5_equal8(self):
        money1 = Money(3)
        money2 = Money(5)

        money_sum = self.adder.add(money1, money2)
        assert money_sum.amount == 8
