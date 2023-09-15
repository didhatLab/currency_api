from src.application.interfaces import CurrencyApi
from src.application import dto


class FakeCurrencyApi(CurrencyApi):
    def __init__(self, fake_rates: dict[str, float | int]) -> None:
        self.rates = fake_rates

    async def get_currency_rate(self, base: str) -> dto.CurrencyRate:
        return dto.CurrencyRate(base=base, rates=self.rates)
