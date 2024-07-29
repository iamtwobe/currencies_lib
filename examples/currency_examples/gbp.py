from currencies_lib import GBP

def main(value = None):
    # Simple usage:
    print(
        GBP(value)
    ) # >> "1,250.51"

    # With decimals:
    print(
        GBP(value, decimals=3)
    ) # >> "1,250.505"

    # With currency symbol:
    print(
        GBP(value, currency_symbol=True)
    ) # >> "£1,250.51"

    # Customized separators:
    print(
        GBP(
            value, thousands_sep='!!', decimal_sep=';;', decimals=3,
            currency_symbol=True
        )
    ) # >> "£1!!250;;505"


if __name__ == "__main__":
    main(1250.505)