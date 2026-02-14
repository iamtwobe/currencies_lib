from functools import wraps
from decimal import Decimal
from .registry import CURRENCIES
import numbers


UNIT_ABBREVIATIONS = {
    1_000: 'k',
    1_000_000: 'M',
    1_000_000_000: 'B',
    1_000_000_000_000: 'T'
}

def _value_check(func):
    @wraps(func)
    def inner(value = None, *args, **kwargs):
        if value is None:
            raise ValueError(f'Missing value for {func.__name__}()')
        if not isinstance(value, numbers.Number):
            raise TypeError(f'Value for {func.__name__}() must be a number, got {type(value)}')

        return func(value, *args, **kwargs)
    return inner

@_value_check
def format_currency(
        value:int|float=None, code:str=None, *, symbol:str=None,
        decimals:int=None, symbol_position:str=None,
        thousands_sep:str=None, decimal_sep:str=None,
        spaced:bool=False
    ) -> str:
    """
        Formats a number as a currency string.

        Parameters
        ----------
        - value (int|float): value to format
        - code (str): currency code in CURRENCIES (ex.: USD, BRL, CHN, EUR...)
        - symbol (str, optional): override currency symbol
        - decimals (int, optional): number of decimal places
        - symbol_position (str, optional): 'LEFT', 'RIGHT', 'L', 'R'
        - thousands_sep (str, optional)
        - decimal_sep (str, optional)
        - spaced (bool, optional): add space between symbol and number

        Example:
        >>> format_currency(1234.56, "USD")
        "$1,234.56"
        >>> format_currency(1234.56, "EUR", symbol_position="R", spaced=True)
        "1,234.56 €"
    """

    currency = CURRENCIES.get(code)
    if not currency:
        raise ValueError(f"Unsupported currency: {code}")

    POSITIONS = {
        'L': 'LEFT',
        'LEFT': 'LEFT',
        'R': 'RIGHT',
        'RIGHT': 'RIGHT'
    }

    symbol = symbol if symbol is not None else currency.symbol
    raw_position = symbol_position or currency.symbol_position
    symbol_position = POSITIONS.get(raw_position.upper())
    if symbol_position is None:
        raise ValueError(f"Invalid symbol_position: {raw_position}")
    
    decimals = decimals if decimals is not None else currency.decimals
    thousands_sep = thousands_sep if thousands_sep is not None else currency.thousands_sep
    decimal_sep = decimal_sep if decimal_sep is not None else currency.decimal_sep
    if thousands_sep == decimal_sep:
        raise ValueError("thousands_sep and decimal_sep cannot be the same")
    _sep = ' ' if spaced else ''

    formatted_value = f"{Decimal(str(value)):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)

    if symbol:
        if symbol_position == 'LEFT':
            formatted_value = f"{symbol}{_sep}{formatted_value}"
        else:
            formatted_value = f"{formatted_value}{_sep}{symbol}"
        
    return formatted_value

def str_to_float(value:str = None) -> float:
    """Translates a string formatted value to float
    (e.g. "$ 1.000,50" to 1000.50)

    Parameters
    ----------
    value : str
        String value to be formatted
    """

    if not value:
        raise ValueError("No value provided")
    
    if not isinstance(value, str):
        raise TypeError("value must be a string")

    allowed_chars = '0123456789.,-'
    value = ''.join(c for c in value if c in allowed_chars)

    if ',' in value and '.' in value:
        if value.rfind(',') > value.rfind('.'):
            value = value.replace('.', '').replace(',', '.')
        else:
            value = value.replace(',', '')

    elif ',' in value:
        value = value.replace(',', '.')
            
    elif '.' in value:
        value = value.replace('.', '')
                    
    return float(value)

@_value_check
def unit_abbreviator(value = None, decimals=1) -> str:
    """Abbreviates a numeric value to its corresponding unit acronym (e.g., 1000 -> 1k).

    Parameters
    ----------
    value : int or float
        numeric value to abbreviate
    decimals : int, optional
        number of decimal places, by default 1

    Returns
    -------
    str
        abbreviated value
        -->> 1k, 1M, 1B, etc.
    """

    for divisor, suffix in sorted(UNIT_ABBREVIATIONS.items(), reverse=True):
        if abs(value) >= divisor:
            abbreviated_value = value / divisor
            return f"{abbreviated_value:.{decimals}f}{suffix}"
        
    return f'{value:.2f}'

@_value_check
def as_percentage(
        value: int|float =None, percent: int | float | str = None, *,
        decimals: int = 2, isfloat: bool = True,
        subtraction: bool = False
    ) -> float:
    """Converts or adjusts a numeric value based on a given percentage.
    
    Can return a percentage of the value (e.g., 25% of 100 = 25) or reduce the value by the specified percentage (e.g., 100 reduced by 25% = 75)

    Parameters
    ----------
    value: int or float
        The value to be formatted
    percent: int or float (or str in cases like "20%")
        The percentage used to format the value

    - Optional Kwargs
    
    subtraction: bool
        Defines if the value should be subtracted by the percentage or not, by default False
    decimals: int
        Defines the decimal places in the final value, by default 2
    isfloat: bool
        Forces the value as a float number, by default True
    """
    if not percent:
        raise ValueError(f"Missing percent: {percent}")
    
    if isinstance(percent, str):
        percent = float(percent.replace("%", "").strip())

    value = float(value)

    if subtraction:
        result = value - (percent * value / 100)
    else:
        result = percent * value / 100

    result = round(result, decimals)

    return float(result) if isfloat else f"{result:.{decimals}f}"