class _Currency_Formater():

    def __init__(self):
        self.nof = "Missing value"
        self.currency_link = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{}.json"
        # ex.: print(self.currency_link.format("usd"))

    def _value_check(func):
        def inner(self, value = None, **kwargs):
            if not value:
                print('\033[91m', f'ERROR: Missing value for "{__class__.__name__} ({func.__name__})"', '\033[0m')
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
    def BRL(self, value = None, *, teste=False) -> str:
        # Definição de métodos de uso a partir de kwargs
        if teste == True:
            print("test success")
        print("BRL", value)

        return "NOTFINISHED"

    @_value_check
    def BRL_to_float(self, value = None) -> float:
        print("Float", value)

        return 1.2

    @_value_check
    def USD(self, value = None) -> str:
        print("USD", value)

        return "NOTFINISHED"

    @_value_check
    def EUR(self, value = None) -> str:
        print("EUR", value)

        return "NOTFINISHED"