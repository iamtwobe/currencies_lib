from currencies_lib import CAD

def main(value = None):
    # Simple usage:
    print(
        CAD(value)
    ) # >> "1,250.51"

    # With decimals:
    print(
        CAD(value, decimals=3)
    ) # >> "1,250.505"

    # With Dolar currency symbol:
    print(
        CAD(value, currency_symbol=True, cad_sign=False)
    ) # >> "$ 1,250.51"

    # With CAD sign:
    print(
        CAD(value, currency_symbol=True)
    ) # >> "C$ 1,250.51"

    # Customized separators:
    print(
        CAD(
            value, thousands_sep='!!', decimal_sep=';;', decimals=3,
            currency_symbol=True, cad_sign=True
        )
    ) # >> "C$ 1!!250;;505"


if __name__ == "__main__":
    main(1250.505)