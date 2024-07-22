from ._currencies import _Currency_Formatter
from ._extra_formatters import _GeneralFormatter

__version__ = "0.2"

Currency_Formatter = _Currency_Formatter()
""" Main documentation will be here soon
"""

GeneralFormatter = _GeneralFormatter()
""" Formatter documentation soon
"""

## Was thinking about using, but performance gets low
# for item in dir(Currency_Formatter):
#     if not item.startswith('_'):
#         globals()[item] = getattr(Currency_Formatter, item)

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

#// ----> General formatter imports <---- \\

as_text = GeneralFormatter.as_text
as_number_base = GeneralFormatter.as_number_base
as_time = GeneralFormatter.as_time