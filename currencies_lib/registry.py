from .currency import Currency


CURRENCIES = {
    "BRL": Currency(
        code="BRL",
        symbol="R$",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "USD": Currency(
        code="USD",
        symbol="$",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "EUR": Currency(
        code="EUR",
        symbol="€",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "RUB": Currency(
        code="RUB",
        symbol="₽",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "GBP": Currency(
        code="GBP",
        symbol="£",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "JPY": Currency(
        code="JPY",
        symbol="¥",
        thousands_sep=",",
        decimal_sep=".",
        decimals=0,
        symbol_position="left",
        spaced=False
    ),
    "CAD": Currency(
        code="CAD",
        symbol="C$",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "AUD": Currency(
        code="AUD",
        symbol="A$",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "CHF": Currency(
        code="CHF",
        symbol="₣",
        thousands_sep="'",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "CNY": Currency(
        code="CNY",
        symbol="¥",
        thousands_sep=",",
        decimal_sep=".",
        decimals=0,
        symbol_position="left",
        spaced=False
    ),
    "NZD": Currency(
        code="NZD",
        symbol="NZ$",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "MXN": Currency(
        code="MXN",
        symbol="MX$",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "SGD": Currency(
        code="SGD",
        symbol="S$",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "SEK": Currency(
        code="SEK",
        symbol="kr",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="right",
        spaced=False
    ),
    "NOK": Currency(
        code="NOK",
        symbol="kr",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="right",
        spaced=False
    ),
    "DKK": Currency(
        code="DKK",
        symbol="kr",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="right",
        spaced=False
    ),
    "PLN": Currency(
        code="PLN",
        symbol="zł",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="right",
        spaced=False
    ),
    "TRY": Currency(
        code="TRY",
        symbol="₺",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "HKD": Currency(
        code="HKD",
        symbol="HK$",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "ILS": Currency(
        code="ILS",
        symbol="₪",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "KRW": Currency(
        code="KRW",
        symbol="₩",
        thousands_sep=",",
        decimal_sep=".",
        decimals=0,
        symbol_position="left",
        spaced=False
    ),
    "RMB": Currency(
        code="RMB",
        symbol="¥",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "COP": Currency(
        code="COP",
        symbol="$",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "ARS": Currency(
        code="ARS",
        symbol="AR$",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "AED": Currency(
        code="AED",
        symbol="AED",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "ZAR": Currency(
        code="ZAR",
        symbol="R",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "THB": Currency(
        code="THB",
        symbol="฿",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "SAR": Currency(
        code="SAR",
        symbol="SR",
        thousands_sep=".",
        decimal_sep=",",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "XCD": Currency(
        code="XCD",
        symbol="EC$",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "XOF": Currency(
        code="XOF",
        symbol="XOF",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="right",
        spaced=False
    ),
    "XAF": Currency(
        code="XAF",
        symbol="XAF",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="right",
        spaced=False
    ),
    "XPF": Currency(
        code="XPF",
        symbol="CFP",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="left",
        spaced=False
    ),
    "DZD": Currency(
        code="DZD",
        symbol="DA",
        thousands_sep=",",
        decimal_sep=".",
        decimals=2,
        symbol_position="right",
        spaced=False
    ),
}