from typing import Self

import attrs
import cattrs


@attrs.define
class CurrencyRate:
    base: str
    rates: dict[str, int | float]

    @classmethod
    def from_dict(cls, raw: dict) -> Self:
        return converter.structure(raw, cls)
    

converter = cattrs.Converter()
converter.register_structure_hook(float | int, lambda value, _: value)
