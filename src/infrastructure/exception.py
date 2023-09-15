class BaseCurrencyApiError(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg


class InvalidBaseRate(BaseCurrencyApiError):
    pass
