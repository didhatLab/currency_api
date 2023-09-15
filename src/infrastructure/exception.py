class BaseCurrencyApiError(Exception):
    def __init__(self, msg: str) -> None:
        set.msg = msg


class InvalidBaseRate(BaseCurrencyApiError):
    pass

