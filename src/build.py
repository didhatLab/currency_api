import aiohttp
from fastapi import FastAPI

from src.presentation.route import api
from src.application.currency import CurrencyRateService
from src.infrastructure.config import AppConfig
from src.infrastructure.currency_api import FreeOpenExchangerCurrencyApi
from src.presentation.providers import get_currency_service
from src.presentation.middleware import setup_middlewares


async def build_app():
    config = AppConfig()

    app = FastAPI()
    app.include_router(api)

    session = aiohttp.ClientSession()

    currency_api = FreeOpenExchangerCurrencyApi(session, config.open_exchange_app_id)

    currency_exchange_service = CurrencyRateService(currency_api)

    app.dependency_overrides[get_currency_service] = lambda: currency_exchange_service

    app.on_event("shutdown")(get_resource_cleaner(session))

    setup_middlewares(app)

    return app


def get_resource_cleaner(session: aiohttp.ClientSession):
    async def clean():
        await session.close()

    return clean
