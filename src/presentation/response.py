from pydantic import BaseModel


class CurrencyExchangeResponse(BaseModel):
    value: float
