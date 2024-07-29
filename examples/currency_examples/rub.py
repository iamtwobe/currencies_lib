from currencies_lib import RUB

def main(value = None):
    # Simple usage:
    print(
        RUB(value)
    ) # >> "1.250,51"

    # With decimals:
    print(
        RUB(value, decimals=3)
    ) # >> "1 250,505"

    # With currency symbol:
    print(
        RUB(value, currency_symbol=True)
    ) # >> "₽ 1 250,51"

    # With sign position:
    print(
        RUB(value, currency_symbol=True, sign_position='right')# can be ['l', 'left', 'r', 'right']
    ) # >> "1 250,51 ₽"

    # Customized separators:
    print(
        RUB(
            value, thousands_sep='!!', decimal_sep=';;', decimals=3,
            currency_symbol=True, sign_position='r'
        )
    ) # >> "1!!250;;505 ₽"


if __name__ == "__main__":
    main(1250.505)