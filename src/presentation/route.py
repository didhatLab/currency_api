from fastapi import APIRouter, Query, Depends

from src.presentation.response import CurrencyExchangeResponse
from src.presentation.providers import get_currency_service
from src.application.currency import CurrencyRateService



api = APIRouter()


@api.get("/api/rates")
async def exchange_currency(value: float, to: str, _from: str = Query(alias="from"), currency_service: CurrencyRateService = Depends(get_currency_service)) -> CurrencyExchangeResponse:
    rate = await currency_service.get_converted_value(_from, to, value)
    return CurrencyExchangeResponse(value=rate)