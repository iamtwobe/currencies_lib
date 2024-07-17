from ._currencies import _Currency_Formater

__version__ = "0.1"

Currency_Formater = _Currency_Formater()
""" Main documentation will be here soon
"""

## Was thinking about using, but performance gets low
# for item in dir(Currency_Formater):
#     if not item.startswith('_'):
#         globals()[item] = getattr(Currency_Formater, item)

BRL = Currency_Formater.BRL
USD = Currency_Formater.USD
EUR = Currency_Formater.EUR
RUB = Currency_Formater.RUB
GBP = Currency_Formater.GBP
JPY = Currency_Formater.JPY
CAD = Currency_Formater.CAD
INR = Currency_Formater.INR
custom_format = Currency_Formater.custom_format
str_to_float = Currency_Formater.str_to_float
as_percentage = Currency_Formater.as_percentage