from typing import Final

import aiohttp

from src.infrastructure import exception
from src.application import dto



class OpenExchangerCurrencyApi:
    api: Final = "https://openexchangerates.org/api/"

    def __init__(self, session: aiohttp.ClientSession , token: str) -> None:
        self._session = session
        self._token = token


    async def get_currency_rate(self, base: str):
        async with self._session.get(f"{self.api}/latest.json?app_id={self._token}") as resp:
            resp = await resp.json()

        return self._process_response(resp)

    @staticmethod
    def _process_response(resp: dict):
        if resp.get("error"):
            message = resp.get("message")
            
            if message == "invalid_base":
                raise exception.InvalidBaseRate(message)
            else:
                raise exception.BaseCurrencyApiError(message)
        
        return dto.CurrencyRate.from_dict(resp)

            

