from functools import wraps

class _Currency_Formatter():

    def __init__(self):
        self.symbols = r" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz$£¢<>?!%&*(){}[]-=+~^|/"
        self.unit_abbreviator_dict = {1_000: 'k', 1_000_000: 'M', 1_000_000_000: 'B', 1_000_000_000_000: 'T'}
        self.right_positions = ["right", "r"]
        self.left_positions = ["left", "l"]
        self._currency_ban_symbols = r"ABCDEFGHIJKLMNOPQRSTUVWXYZ€₽£¥"
        self.currencies = {
            '$': 'USD',     'USD':'USD',
            'R$': 'BRL',    'BRL':'BRL',
            '€': 'EUR',     'EUR':'EUR',
            '₽': 'RUB',     'RUB':'RUB',
            '£': 'GBP',     'GBP':'GBP',
            '¥': 'JPY',     'JPY':'JPY',
            'C$': 'CAD',    'CAD':'CAD',
            '₹': 'INR',     'INR':'INR'
        }
        
        # ex.: print(self.currency_link.format("usd"))

    def _value_check(func):
        @wraps(func)
        def inner(self, value = None, *args, **kwargs):
            try:
                if not value:
                    print('\033[91m' + f'ERROR: Missing value for "Currency Formatter.{func.__name__}()"', '\033[0m')
                    return None
                if type(value) in (float, int):
                    pass
                else:
                    raise ValueError
            except ValueError:
                print(f'Currency Formatter: The inputted value is not a Integer or a Float. ("{type(value)}")')
                return None
            
            try:
                function_exec = func(self, value, **kwargs)
                return function_exec
            except Exception as e:
                print(e)
            return
        return inner

    @_value_check
    def as_percentage(self, value = None, percent = None, *, decimals=2, isfloat=True, subtraction=False) -> float:
        # Usage: as_percentage(value=100, percentage="25%") -> 25
        try:
            if not percent:
                print('Currency Formatter: The percentage value is missing.')
                return None
            if isinstance(percent, str):
                percent = float(percent.replace("%", ""))
            match subtraction:
                case True:
                    final_value = f"{value - (percent * float(value) / 100):.{decimals}f}"
                case False:
                    final_value = f"{percent * float(value) / 100:.{decimals}f}"

            if isfloat == True:
                return float(final_value)
            return final_value
        
        except Exception as e:
            print(e)
        
        return None

    @_value_check
    def custom_format(self, value = None, *, currency_symbol: str=None,
            sign_position: str='LEFT',
            thousands_sep: str=',', decimal_sep: str='.',
            custom_format=None) -> str:

        if not custom_format:
            print(f'Currency Formatter: Format must be provided.')
            return None
        if type(custom_format) != str:
            print(f'Currency Formatter: The inputted format is not a String type. ("{type(custom_format)}")')
            return None
        if len(custom_format) < 1:
            print(f'Currency Formatter: The inputted format is empty. ("{custom_format}")')
            return None
        if decimal_sep == custom_format[:1]:
            print(f'Currency Formatter: The decimal_sep cannot be the same as the custom_format. ("{decimal_sep}")')
            return None
        
        try:
            sign_position = sign_position.lower()
            if sign_position not in self.right_positions and sign_position not in self.left_positions:
                print(f'Currency Formatter: Invalid sign_position inputted. ("{sign_position}")')
                return None
            
            if sign_position in self.right_positions:
                sign_position = "RIGHT"
            elif sign_position in self.left_positions:
                sign_position = "LEFT"
            else:
                raise ReferenceError

            match sign_position:
                case "RIGHT":
                    final_value = f"{float(value):{custom_format}}{(" " + currency_symbol) if currency_symbol != None else ""}"
                    final_value = final_value.replace('.', decimal_sep).replace(f'{custom_format[:1]}', thousands_sep)
                case "LEFT":
                    final_value = f"{(currency_symbol + " ") if currency_symbol != None else ""}{float(value):{custom_format}}"
                    final_value = final_value.replace('.', decimal_sep).replace(f'{custom_format[:1]}', thousands_sep)
            
            return final_value
        
        except ValueError:
            print(f'Currency Formatter: Invalid format inputted. ("{custom_format[0]}")')

        except ReferenceError:
            print(f'Currency Formatter: The inputted position is not valid. Must be left or right. ("{sign_position}")')

        except Exception as e:
            print(f'Currency Formatter (Unexpected): {e}')

        return None
   
    @_value_check
    def unit_abbreviator(self, value, decimals=1) -> str:
        # 1000 as > 1k || 1000000 as > 1M
        try:
            for divisor, suffix in sorted(self.unit_abbreviator_dict.items(), reverse=True):
                if abs(value) >= divisor:
                    abbreviated_value = value / divisor
                    return f"{abbreviated_value:.{decimals}f}{suffix}"
            return f'{value:.2f}'
        
        except Exception as e:
            print(e)

        return None

    @_value_check
    def format_currency(self, value = None, *, currency_symbol='',
            sign_position='left', thousands_sep=',',
            decimal_sep='.', decimals=2):
        
        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_symbol:
                if sign_position in self.right_positions:
                    sign_position = "RIGHT"
                elif sign_position in self.left_positions:
                    sign_position = "LEFT"
                else:
                    raise ReferenceError
                match sign_position:
                    case 'LEFT':
                        final_value = f"{currency_symbol}{final_value}"
                    case 'RIGHT':
                        final_value = f"{final_value}{currency_symbol}"

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except ReferenceError:
            print(f'Currency Formatter: The inputted position is not valid. Must be left or right. ("{sign_position}")')

        except Exception as e:
            print(e)

        return None

    def detect_currency(self, value):
        # Can be imprecise. Needs more tests
        try:
            for symbol, currency in self.currencies.items():
                if symbol in value and not value[(value.rfind(symbol)-1)] in self._currency_ban_symbols:
                    return currency
            raise RuntimeError

        except RuntimeError:
            print(f'Currency Formatter: Unable to detect the currency of "{value}"')

        except Exception as e:
            print(e)
        
        return None

    def str_to_float(self, value = None) -> float:
        # Can be imprecise
        try:
            if not value:
                raise ValueError("Currency Formatter: The value must be provided")
            __number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            for i, __none in enumerate(value):
                if value[i] in __number_list:
                    negative_num = False
                    break

                if value[i] == '-':
                    negative_num = True
                    break

            if any(char in value for char in self.symbols):
                for char in self.symbols:
                    value = value.replace(char, '')

            if ',' in value and '.' in value:
                if value.rfind(',') > value.rfind('.'):
                    value = value.replace('.', '')
                    value = value.replace(',', '.')
                else:
                    value = value.replace(',', '')

            elif ',' in value:
                value = value.replace(',', '.')
            
            elif '.' in value:
                value = value.replace('.', '')
            
            if negative_num:
                final_value = float('-' + value)
                return final_value
                    
            final_value = float(value)
            return final_value

        except ValueError:
            print(f"Currency Formatter: Unable to convert '{value}' to float")
                    
        except Exception as e:
            print("Currency Formatter:", e)
        
        return None

    @_value_check
    def BRL(self, value = None, *, thousands_sep: str = '.',
            decimal_sep: str = ',',
            currency_symbol=False, decimals=2) -> str:
        # You can define the decimal places (default = 2)
        # You can define if you want the currency sign (default = False)

        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_symbol == True:
                final_value = f"R$ {final_value}"             

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except Exception as e:
            print(e)

        return None

    @_value_check
    def USD(self, value = None, *, thousands_sep: str = ',',
            decimal_sep: str = '.',
            currency_symbol=False, decimals=2) -> str:
        # You can define the decimal places (default = 2)
        # You can define if you want the currency sign (default = False)

        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_symbol == True:
                final_value = f"$ {final_value}"

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except Exception as e:
            print(e)

        return None

    @_value_check
    def EUR(self, value = None, *, thousands_sep: str = '.',
            decimal_sep: str = ',', sign_position="LEFT",
            currency_symbol=False, eur_sign=False, decimals=2) -> str:
        # You can define the decimal places (default = 2)
        # You can define if you want the currency sign (default = False)

        try:
            sign_position = sign_position.lower()
            if sign_position not in self.right_positions and sign_position not in self.left_positions:
                print(f'Currency Formatter: Invalid sign_position inputted. ("{sign_position}")')
                return None
            
            if sign_position in self.right_positions:
                sign_position = "RIGHT"
            elif sign_position in self.left_positions:
                sign_position = "LEFT"
            else:
                raise ReferenceError

            if currency_symbol == True:
                if eur_sign == True:
                    eur_sign = "€"
                elif eur_sign == False:
                    eur_sign = "EUR"

                match sign_position:
                    case "RIGHT":
                        final_value = f"{float(value):_.{decimals}f} {eur_sign}".replace('.', decimal_sep).replace('_', thousands_sep)
                    case "LEFT":
                        final_value = f"{eur_sign} {float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            else:
                final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except ReferenceError:
            print(f'Currency Formatter: The inputted position is not valid. Must be left or right. ("{sign_position}")')

        except Exception as e:
            print(e)

        return None
    
    @_value_check
    def RUB(self, value = None, *, thousands_sep: str = ' ',
            decimal_sep: str = ',',
            currency_symbol=False, sign_position="LEFT", decimals=2) -> str:
        # You can define the decimal places (default = 2)
        # You can define if you want the currency sign (default = False)

        try:
            sign_position = sign_position.lower()
            if sign_position not in self.right_positions and sign_position not in self.left_positions:
                print(f'Currency Formatter: Invalid sign_position inputted. ("{sign_position}")')
                return None
            
            if sign_position in self.right_positions:
                sign_position = "RIGHT"
            elif sign_position in self.left_positions:
                sign_position = "LEFT"
            else:
                raise ReferenceError

            if currency_symbol == True:
                match sign_position:
                    case "RIGHT":
                        final_value = f"{float(value):_.{decimals}f} ₽".replace('.', decimal_sep).replace('_', thousands_sep)
                    case "LEFT":
                        final_value = f"₽ {float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            else:
                final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except ReferenceError:
            print(f'Currency Formatter: The inputted position is not valid. Must be left or right. ("{sign_position}")')

        except Exception as e:
            print(e)

        return None
    
    @_value_check
    def GBP(self, value = None, *, thousands_sep: str = ',',
            decimal_sep: str = '.',
            currency_symbol=False, decimals=2) -> str:

        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_symbol == True:
                final_value = f"£{final_value}"

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except Exception as e:
            print(e)

        return None

    @_value_check
    def JPY(self, value = None, *, thousands_sep: str = ',',
            currency_symbol=False) -> str:

        try:
            final_value = f"{float(value):_.0f}".replace('_', thousands_sep)
            if currency_symbol == True:
                final_value = f"¥{final_value}"

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep}")')
        
        except Exception as e:
            print(e)

        return None

    @_value_check
    def CAD(self, value = None, *, thousands_sep: str = ',',
            decimal_sep: str = '.', spaced_sign=True,
            currency_symbol=False, cad_sign=True, decimals=2) -> str:

        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_symbol == True:
                match cad_sign:
                    case True:
                        cad_sign = "C$"
                    case False:
                        cad_sign = "$"
                if spaced_sign == True:
                    cad_sign += " "

                final_value = f"{cad_sign}{final_value}"
                
            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except Exception as e:
            print(e)

        return None

    @_value_check
    def INR(self, value = None, *, thousands_sep: str = ',',
            decimal_sep: str = '.',
            currency_symbol=None, decimals=2) -> str:

        try:
            if value >= 100000 or value <= -100000:
                if str(value).startswith('-'):
                    negative_num = True
                    value = str(value)[1:]
                else:
                    negative_num = False
                if '.' in str(value):
                    int_value, dec_value = f'{float(value):.2f}'.split('.')
                else:
                    int_value = f'{value}'
                    dec_value = None
                if len(int_value) > 3:
                    int_value = int_value[::-1]
                    int_value = [int_value[:3]] + [int_value[i:i + 2] for i in range(3, len(int_value), 2)]
                    int_value = thousands_sep.join(int_value)[::-1]

                final_value = (
                    ('-' if negative_num else '') + int_value +
                    (decimal_sep + dec_value if dec_value else decimal_sep +('0' * decimals))
                )
                if currency_symbol:
                    final_value = f'₹{final_value}'
                    
                return final_value

            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_symbol:
                final_value = f'₹{final_value}'

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep}")')
        
        except Exception as e:
            print(e)

        return None