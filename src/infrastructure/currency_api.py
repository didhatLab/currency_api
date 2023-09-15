from typing import Final, cast

import aiohttp

from src.infrastructure import exception
from src.application import dto


class FreeOpenExchangerCurrencyApi:
    api: Final = "https://openexchangerates.org/api/"

    def __init__(self, session: aiohttp.ClientSession, token: str) -> None:
        self._session = session
        self._token = token

    async def get_currency_rate(self, base: str) -> dto.CurrencyRate:
        async with self._session.get(
            f"{self.api}/latest.json?app_id={self._token}"
        ) as resp:
            json_resp = await resp.json()

        rate = self._process_response(json_resp)

        if rate.base != base:
            right_base = rate.rates.get(base)
            if right_base is None:
                raise exception.InvalidBaseRate("invalid base")

            new_rates = {}

            for currency, r in rate.rates.items():
                new_rates[currency] = right_base * 100 / (r * 100)

            rate = dto.CurrencyRate(base=base, rates=new_rates)

        return rate

    @staticmethod
    def _process_response(resp: dict) -> dto.CurrencyRate:
        if resp.get("error"):
            message = cast(str, resp.get("message"))

            if message == "invalid_base":
                raise exception.InvalidBaseRate(message)
            else:
                raise exception.BaseCurrencyApiError(message)

        return dto.CurrencyRate.from_dict(resp)
