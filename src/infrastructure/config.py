from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    open_exchange_app_id: str = "qwerty"