from fastapi import APIRouter, Query, Depends

from src.application.currency import CurrencyRateService
from src.presentation.response import CurrencyExchangeResponse


api = APIRouter()


@api.get("api/rates")
async def exchange_currency(to: str,  _from: str = Query(alias="from"), currency_service: CurrencyRateService = Depends(CurrencyRateService)) -> CurrencyExchangeResponse:
    rate = currency_service.get_currency_rate(_from, to)
    
    return CurrencyExchangeResponse(rate)