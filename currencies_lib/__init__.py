from .currencies import Currency_Formatter

__version__ = "0.6"



#// ----> Function imports <---- \\
Currency_Formatter = Currency_Formatter()

str_to_float = Currency_Formatter.str_to_float
as_percentage = Currency_Formatter.as_percentage
unit_abbreviator = Currency_Formatter.unit_abbreviator
format_currency = Currency_Formatter.format_currency
detect_currency = Currency_Formatter.detect_currency
custom_format = Currency_Formatter.custom_format
unspecified_currency = Currency_Formatter.unspecified_currency
(
    BRL, USD, EUR, RUB, GBP, JPY, CAD, INR, AUD, CHF,
    CNY, NZD, MXN, SGD, SEK, NOK, PLN, TRY, HKD, ILS,
    KRW, RMB, COP, ARS, AED, ZAR, THB, SAR, DZD, XPF,
    XAF, XOF, XCD
) = (getattr(Currency_Formatter, currency) for currency in [
    'BRL', 'USD', 'EUR', 'RUB', 'GBP', 'JPY', 'CAD', 'INR',
    'AUD', 'CHF', 'CNY', 'NZD', 'MXN', 'SGD', 'SEK', 'NOK',
    'PLN', 'TRY', 'HKD', 'ILS', 'KRW', 'RMB', 'COP', 'ARS',
    'AED', 'ZAR', 'THB', 'SAR', 'DZD', 'XPF', 'XAF', 'XOF',
    'XCD'
])