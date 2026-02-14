from .formatter import format_currency


def _make_currency_function(code):
    def wrapper(
        value:int|float=None, *, symbol:str=None,
        decimals:int=None, symbol_position:str=None,
        thousands_sep:str=None, decimal_sep:str=None,
        spaced:bool=False
    ) -> str:
        return format_currency(
            value, code,
            symbol=symbol,
            decimals=decimals,
            symbol_position=symbol_position,
            thousands_sep=thousands_sep,
            decimal_sep=decimal_sep,
            spaced=spaced
        )
    wrapper.__name__ = code
    wrapper.__doc__ = format_currency.__doc__
    return wrapper

all_currencies = [
    "BRL", "USD", "EUR", "RUB", "GBP", "JPY", "CAD", "AUD", "CHF", 
    "CNY", "NZD", "MXN", "SGD", "SEK", "NOK", "DKK", "PLN", "TRY",
    "HKD", "ILS", "KRW", "RMB", "COP", "ARS", "AED", "ZAR", "THB", 
    "SAR", "XCD", "XOF", "XAF", "XPF", "DZD"
]

BRL = _make_currency_function("BRL")
USD = _make_currency_function("USD")
EUR = _make_currency_function("EUR")
RUB = _make_currency_function("RUB")
GBP = _make_currency_function("GBP")
JPY = _make_currency_function("JPY")
CAD = _make_currency_function("CAD")
AUD = _make_currency_function("AUD")
CHF = _make_currency_function("CHF")
CNY = _make_currency_function("CNY")
NZD = _make_currency_function("NZD")
MXN = _make_currency_function("MXN")
SGD = _make_currency_function("SGD")
SEK = _make_currency_function("SEK")
NOK = _make_currency_function("NOK")
DKK = _make_currency_function("DKK")
PLN = _make_currency_function("PLN")
TRY = _make_currency_function("TRY")
HKD = _make_currency_function("HKD")
ILS = _make_currency_function("ILS")
KRW = _make_currency_function("KRW")
RMB = _make_currency_function("RMB")
COP = _make_currency_function("COP")
ARS = _make_currency_function("ARS")
AED = _make_currency_function("AED")
ZAR = _make_currency_function("ZAR")
THB = _make_currency_function("THB")
SAR = _make_currency_function("SAR")
XCD = _make_currency_function("XCD")
XOF = _make_currency_function("XOF")
XAF = _make_currency_function("XAF")
XPF = _make_currency_function("XPF")
DZD = _make_currency_function("DZD")