import abc
from typing import Protocol

from src.application import dto


class CurrencyApi(Protocol):
    @abc.abstractmethod
    async def get_currency_rate(self, base: str) -> dto.CurrencyRate:
        pass
