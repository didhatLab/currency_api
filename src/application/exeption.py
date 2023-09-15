

class NotFoundCurrencyForExchange(Exception):
    pass


class CurrencyApiError(Exception):

    def __init__(self, error: str):
        self.error = error