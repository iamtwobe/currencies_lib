from ._currencies import _Currency_Formatter

__version__ = "0.3"

Currency_Formatter = _Currency_Formatter()
""" Main documentation will be here soon
"""

## Was thinking about using, but performance gets low
# for item in dir(Currency_Formatter):
#     if not item.startswith('_'):
#         globals()[item] = getattr(Currency_Formatter, item)


#// ----> Function imports <---- \\

BRL = Currency_Formatter.BRL
USD = Currency_Formatter.USD
EUR = Currency_Formatter.EUR
RUB = Currency_Formatter.RUB
GBP = Currency_Formatter.GBP
JPY = Currency_Formatter.JPY
CAD = Currency_Formatter.CAD
INR = Currency_Formatter.INR
custom_format = Currency_Formatter.custom_format
str_to_float = Currency_Formatter.str_to_float
as_percentage = Currency_Formatter.as_percentage
unit_abbreviator = Currency_Formatter.unit_abbreviator
format_currency = Currency_Formatter.format_currency