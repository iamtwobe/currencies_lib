from currencies_lib import EUR

def main(value = None):
    # Simple usage:
    print(
        EUR(value)
    ) # >> "1.250,51"

    # With decimals:
    print(
        EUR(value, decimals=3)
    ) # >> "1.250,505"

    # With currency symbol:
    print(
        EUR(value, currency_symbol=True)
    ) # >> "EUR 1.250,51"

    # With euro sign:
    print(
        EUR(value, currency_symbol=True, eur_sign=True)
    ) # >> "€ 1.250,51"

    # With sign position:
    print(
        EUR(value, currency_symbol=True, eur_sign=True, sign_position='right') # can be ['l', 'left', 'r', 'right']
    ) # >> "1.250,51 €"

    # Customized separators:
    print(
        EUR(
            value, thousands_sep='!!', decimal_sep=';;', decimals=3,
            currency_symbol=True, eur_sign=True, sign_position='left'
        )
    ) # >> "€ 1!!250;;505"


if __name__ == "__main__":
    main(1250.505)