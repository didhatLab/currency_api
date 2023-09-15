import aiohttp
from fastapi import FastAPI

from src.presentation.route import api
from src.application.currency import CurrencyRateService
from src.infrastructure.config import AppConfig 
from src.infrastructure.currency_api import OpenExchangerCurrencyApi


def build_app():
    config = AppConfig()

    app = FastAPI()
    api.include_router(api)

    session = aiohttp.ClientSession()

    currency_api = OpenExchangerCurrencyApi(session, config.open_exchange_app_id)
    
    currency_exchange_service = CurrencyRateService(currency_api)


    app.dependency_overrides[CurrencyRateService] = currency_exchange_service

    app.on_event("shutdown")(get_resource_cleaner())

    return app


def get_resource_cleaner(session: aiohttp.ClientSession):

    async def clean():
        await session.close()

    return clean
    
