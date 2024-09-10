from money.exchange_service import ExchangeService
from money.money import Money
from money.money_adder import MoneyAdder
from money.currency_type import CurrencyType
from tests.exchange_service_stub import ExchangeServiceStub


class TestMoney:
    exchange_service_stub = ExchangeServiceStub()

    def test_2and4_equals6(self):
        money1 = Money(4, CurrencyType.USD)
        money2 = Money(2, CurrencyType.USD)

        adder = MoneyAdder(self.exchange_service_stub)
        money_sum = adder.add(money1, money2)
        assert money_sum.amount == 6

    def test_3and5_equals8(self):
        money1 = Money(3, CurrencyType.USD)
        money2 = Money(5, CurrencyType.USD)

        adder = MoneyAdder(self.exchange_service_stub)
        money_sum = adder.add(money1, money2)
        assert money_sum.amount == 8

    def test_4usd_and_2eur_equals8usd(self):
        money1 = Money(4, CurrencyType.USD)
        money2 = Money(2, CurrencyType.EUR)

        adder = MoneyAdder(self.exchange_service_stub)
        money_sum = adder.add(money1, money2)
        assert money_sum.amount == 8

    def test__4usd_and_2eur_equals10usd_mock(self, mocker):
        money1 = Money(4, CurrencyType.USD)
        money2 = Money(2, CurrencyType.EUR)

        mocker.patch('money.exchange_service.ExchangeService.convert', return_value=6)
        exchange_service = ExchangeService()
        adder = MoneyAdder(exchange_service)
        money_sum = adder.add(money1, money2)
        assert money_sum.amount == 10
