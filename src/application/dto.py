from typing import Self

import attrs
import cattrs


@attrs.define
class CurrencyRate:
    base: str
    rates: dict[str, int | float]

    @classmethod
    def from_dict(cls, raw: dict) -> Self:
        return cattrs.structure(raw, cls)
    
    