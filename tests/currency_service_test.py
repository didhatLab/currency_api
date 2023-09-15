import pytest

from tests import fake
from src.application.currency import CurrencyRateService
from src.application.exeption import CurrencyApiError


@pytest.fixture()
def currency_api():
    return fake.FakeCurrencyApi({"USD": 80, "RUB": 1, "EUR": 900})


@pytest.fixture
def converter_service(currency_api) -> CurrencyRateService:
    return CurrencyRateService(currency_api=currency_api)


async def test_basic_convert(converter_service: CurrencyRateService):
    res = await converter_service.get_converted_value("USD", "RUB", 5)

    assert res == 400


async def test_try_convert_non_exist_currency(converter_service: CurrencyRateService):
    with pytest.raises(CurrencyApiError):
        await converter_service.get_converted_value("iDD", "RUB", 5)
