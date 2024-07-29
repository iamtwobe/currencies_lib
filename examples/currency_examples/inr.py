from currencies_lib import INR

def main(value = None):
    # Simple usage:
    print(
        INR(value)
    ) # >> "1,250.51"

    # With decimals:
    print(
        INR(value, decimals=3)
    ) # >> "1,250.505"

    # With INR sign:
    print(
        INR(value, currency_symbol=True)
    ) # >> "₹1,250.51"

    # Customized separators:
    print(
        INR(
            value, thousands_sep='!!', decimal_sep=';;', decimals=3,
            currency_symbol=True
        )
    ) # >> "₹1!!250;;505"

    # Bigger values:
    print(
        INR(1000000, currency_symbol=True)
    ) # >> "₹10,00,000.00"


if __name__ == "__main__":
    main(1250.505)