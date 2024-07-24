import re
from functools import wraps

class _Currency_Formatter():

    def __init__(self):
        self.symbols = r" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz$£¢<>?!%&*(){}[]-=+~^|/"
        self.right_positions = ["right", "r"]
        self.left_positions = ["left", "l"]
        self.currency_link = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{}.json"
        
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
            function_exec = func(self, value, **kwargs)
            return function_exec
        return inner
    
    def _currency_data_check(func):
        # Decorator to check and get the API values
        @wraps(func)
        def inner(self, value = None, **kwargs):
            print("!!!!!!!!!")
        return inner
    
    def _format_api_link(self, currency):
        #may be useles actually
        return self.currency_link.format(currency)

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
    def custom_format(self, value = None, *, currency_sign: str=None,
            sign_position: str='LEFT',
            thousands_sep: str=',', decimal_sep: str='.',
            custom_format=None) -> str:
        
        ''' esse módulo faz isso aqui
        
        >> pew pwew
        - `aaha(a, b)` - hihihiha.
        '''
        
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
                    final_value = f"{float(value):{custom_format}}{(" " + currency_sign) if currency_sign != None else ""}"
                    final_value = final_value.replace('.', decimal_sep).replace(f'{custom_format[:1]}', thousands_sep)
                case "LEFT":
                    final_value = f"{(currency_sign + " ") if currency_sign != None else ""}{float(value):{custom_format}}"
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
    def unit_abbreviator(self, value = None):
        # 1000 as > 1k || 1000000 as > 1M 
        pass

    @_value_check
    def format_currency(self, value = None, *, currency_sign='',
            sign_position='left', thousands_sep=',',
            decimal_sep='.', decimals=2):
        
        try:
            
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_sign:
                if sign_position in self.right_positions:
                    sign_position = "RIGHT"
                elif sign_position in self.left_positions:
                    sign_position = "LEFT"
                else:
                    raise ReferenceError
                match sign_position:
                    case 'LEFT':
                        final_value = f"{currency_sign} {final_value}"
                    case 'RIGHT':
                        final_value = f"{final_value} {currency_sign}"

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except ReferenceError:
            print(f'Currency Formatter: The inputted position is not valid. Must be left or right. ("{sign_position}")')

        except Exception as e:
            print(e)

        return None

    def str_to_float(self, value = None) -> float:
        # Can be imprecise
        try:
            if value is None:
                raise ValueError("Currency Formatter: The value must be provided")
            
            if value.startswith('-'):
                negative_num = True
            else:
                negative_num = False

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
            return None
                    
        except Exception as e:
            print(e)
            return None

    @_value_check
    def BRL(self, value = None, *, thousands_sep: str = '.',
            decimal_sep: str = ',',
            currency_sign=False, decimals=2) -> str:
        # You can define the decimal places (default = 2)
        # You can define if you want the currency sign (default = False)

        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_sign == True:
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
            currency_sign=False, decimals=2) -> str:
        # You can define the decimal places (default = 2)
        # You can define if you want the currency sign (default = False)

        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_sign == True:
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
            currency_sign=False, eur_sign=False, decimals=2) -> str:
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

            if currency_sign == True:
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
            currency_sign=False, sign_position="LEFT", decimals=2) -> str:
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

            if currency_sign == True:
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
    
    def GBP(self, value = None, *, thousands_sep: str = ',',
            decimal_sep: str = '.',
            currency_sign=False, decimals=2) -> str:

        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_sign == True:
                final_value = f"£{final_value}"

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except Exception as e:
            print(e)

        return None

    def JPY(self, value = None, *, thousands_sep: str = ',',
            currency_sign=False) -> str:

        try:
            final_value = f"{float(value):_.0f}".replace('_', thousands_sep)
            if currency_sign == True:
                final_value = f"¥{final_value}"

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep}")')
        
        except Exception as e:
            print(e)

        return None

    def CAD(self, value = None, *, thousands_sep: str = ',',
            decimal_sep: str = '.', spaced_sign=True,
            currency_sign=False, cad_sign=True, decimals=2) -> str:

        try:
            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_sign == True:
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

    def INR(self, value = None, *, thousands_sep: str = ',',
            decimal_sep: str = '.',
            currency_sign=None, decimals=2) -> str:

        try:
            if value >= 100000 or value <= 100000:
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
                if currency_sign:
                    final_value = f'₹{final_value}'
                    
                return final_value

            final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            if currency_sign:
                final_value = f'₹{final_value}'

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep}")')
        
        except Exception as e:
            print(e)

        return None