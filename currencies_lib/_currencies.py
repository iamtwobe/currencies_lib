class _Currency_Formater():

    def __init__(self):
        self.nof = "Missing value"
        self.symbols = r" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz$£¢<>?!%&*(){}[]-=+~^|/"
        self.currency_link = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{}.json"
        # ex.: print(self.currency_link.format("usd"))

    def _value_check(func):
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
        def inner(self, value = None, **kwargs):
            print("!!!!!!!!!")
        return inner
    
    def _format_api_link(self, currency):
        return self.currency_link.format(currency)

    @_value_check
    def as_percentage(self, value = None, percent = None, *, decimals=2, isfloat=True, subtraction=False) -> float:
        # Usage: as_percentage(value=100, percentage="25%") -> 25
        try:
            if not percent:
                print(f'Currency Formatter: The percentage value is missing.')
                return None
            if type(percent) == str:
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
            final_value = f"{(currency_sign + " ") if currency_sign != None else ""}{float(value):{custom_format}}"
            final_value = final_value.replace('.', decimal_sep).replace(f'{custom_format[:1]}', thousands_sep)
            
            return final_value
        
        except ValueError:
            print(f'Currency Formatter: Invalid format inputted. ("{custom_format[0]}")')

        except Exception as e:
            print(f'Currency Formatter (Unexpected): {e}')

        return None

    @_value_check
    def BRL(self, value = None, *, thousands_sep: str = '.',
            decimal_sep: str = ',',
            currency_sign=None, decimals=2) -> str:
        # You can define the decimal places (default = 2)
        # You can define if you want the currency sign (default = False)

        # Definição de métodos de uso a partir de kwargs
        try:
            if currency_sign == True:
                final_value = f"R$ {float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)
            else:
                final_value = f"{float(value):_.{decimals}f}".replace('.', decimal_sep).replace('_', thousands_sep)

            return final_value
        
        except TypeError:
            print(f'Currency Formatter: The inputted value is not a String type. ("{thousands_sep if type(thousands_sep) != str else decimal_sep}")')
        
        except Exception as e:
            print(e)

        return None

    def str_to_float(self, value = None) -> float:
        # Can be imprecise
        try:
            if value is None:
                raise ValueError("Currency Formatter: The value must be provided")
            
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
                pass
            
        except Exception as e:
            print(e)
            return None

        try:
            final_value = float(value)
            return final_value
        except ValueError:
            raise ValueError(f"Currency Formatter: Unable to convert '{value}' to float")

        return None

    @_value_check
    def USD(self, value = None) -> str:
        print("USD", value)

        return "NOTFINISHED"

    @_value_check
    def EUR(self, value = None) -> str:
        print("EUR", value)

        return "NOTFINISHED"