from fastapi import APIRouter, Query, Depends

from src.presentation.response import CurrencyExchangeResponse
from src.presentation.providers import get_currency_service



api = APIRouter()


@api.get("/api/rates")
async def exchange_currency(to: str,  _from: str = Query(alias="from"), currency_service = Depends(get_currency_service)) -> CurrencyExchangeResponse:
    rate = currency_service.get_currency_rate(_from, to)
    
    return CurrencyExchangeResponse(rate)