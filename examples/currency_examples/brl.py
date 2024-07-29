from currencies_lib import BRL

def main(value = None):
    # Simple usage:
    print(
        BRL(value)
    ) # >> "1.250,51"

    # With decimals:
    print(
        BRL(value, decimals=3)
    ) # >> "1.250,505"

    # With currency symbol:
    print(
        BRL(value, currency_symbol=True)
    ) # >> "R$ 1.250,51"

    # Customized separators:
    print(
        BRL(value, thousands_sep='!!', decimal_sep=';;', decimals=3, currency_symbol=True)
    ) # >> "R$ 1!!250;;505"


if __name__ == "__main__":
    main(1250.505)