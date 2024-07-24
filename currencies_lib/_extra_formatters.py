from functools import wraps

class _GeneralFormatter():

    def __init__(self):
        self.symbols = r" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz$£¢<>?!%&*(){}[]-=+~^|/"
        self.right_positions = ["right", "r"]
        self.left_positions = ["left", "l"]

    def _value_check(func):
        @wraps(func)
        def inner(self, value = None, *args, **kwargs):
            try:
                if not value:
                    print('\033[91m' + f'ERROR: Missing value for "General Formatter.{func.__name__}()"', '\033[0m')
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
    
    @_value_check
    def as_time(self, value = None):
        # 120 as > 2 minutes || 3661 as > 1h 1m 1s
        pass

    @_value_check
    def as_text(self, value = None):
        # 123 as > one hundred twenty-three || 1000 as > one thousand
        pass

    @_value_check
    def as_number_base(self, value = None):
        # value to > binary, hexadecimal, octal
        pass

    @_value_check
    def as_scientific(self, value, *, decimals=2):
        # 1000 as > 10³
        pass

    @_value_check
    def as_roman_numeral(self, value):
        # 10 as > X
        pass

    @_value_check
    def as_phone_number(self, value, *, country_code=""):
        # 00, 123456789 as > +00 123456789
        pass

    @_value_check
    def as_metric(self, value):
        # 100 as > 100 cm || > 100 m || > 100 km
        pass