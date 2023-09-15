from src.application.interfaces import CurrencyApi
from src.infrastructure.exception import BaseCurrencyApiError, InvalidBaseRate
from src.application.exeption import NotFoundCurrencyForExchange, CurrencyApiError


class CurrencyRateService:
    def __init__(self, currency_api: CurrencyApi):
        self._currency_api = currency_api

    async def get_converted_value(self, _from: str, to: str, value: int):
        try:
            converted_value = await self._get_converted_value(_from, to, value)
        except InvalidBaseRate:
            raise CurrencyApiError("invalid to currency")
        except BaseCurrencyApiError:
            raise CurrencyApiError("external currency api error")
        except NotFoundCurrencyForExchange:
            raise CurrencyApiError("not found from currency")
        return converted_value

    async def _get_converted_value(self, _from: str, to: str, value: float):
        rate = await self._currency_api.get_currency_rate(to)

        from_rate = rate.rates.get(_from)

        if from_rate is None:
            raise NotFoundCurrencyForExchange()

        return from_rate * value
