from dataclasses import dataclass


@dataclass(frozen=True)
class Currency:
    code: str
    symbol: str
    thousands_sep: str
    decimal_sep: str
    decimals: int
    symbol_position: str # LEFT or RIGHT
    spaced: bool