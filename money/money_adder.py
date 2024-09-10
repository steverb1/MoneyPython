from money.currency_type import CurrencyType
from money.money import Money


class MoneyAdder:
    def __init__(self, exchange_service):
        self.exchange_service = exchange_service

    def add(self, money1, money2):
        if money1.currency_type == money2.currency_type:
            return Money(money1.amount + money2.amount, money1.currency_type)

        converted_amount = self.exchange_service.convert(money2.amount, money2.currency_type, money1.currency_type)
        return Money(money1.amount + converted_amount, money1.currency_type)
