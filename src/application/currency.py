from src.application.interfaces import CurrencyApi
from src.infrastructure.exception import BaseCurrencyApiError, InvalidBaseRate
from src.application.exeption import NotFoundCurrencyForExchange, CurrencyApiError


class CurrencyRateService:
    def __init__(self, currency_api: CurrencyApi):
        self._currency_api = currency_api

    async def get_currency_rate(self, _from: str, to: str):
        try:
            rate = await self._get_currency_rate(_from, to) 
        except InvalidBaseRate as e:
            raise CurrencyApiError("invalid from currency")
        except BaseCurrencyApiError as e:
            raise CurrencyApiError("external currency api error")
        except NotFoundCurrencyForExchange as e:
            raise CurrencyApiError("not found to currency")
        return rate

    async def _get_currency_rate(self, _from: str, to: str):
        rate = await self._currency_api.get_currency_rate(_from)

        to_rate = rate.rates.get(to)

        if to_rate is None:
            raise NotFoundCurrencyForExchange()

        return to_rate