from money.money import Money


class MoneyAdder:
    def add(self, money1, money2):
        return Money(money1.amount + money2.amount)
