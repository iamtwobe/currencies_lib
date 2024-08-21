from currencies_lib import EUR

def main(value = None):
    """
    All other currencies use the same types of args.
    Some might have less kwargs than the "EUR", because Euro uses lots of formats,
        including left or right positions or EUR/€ sign.
    
    EUR is being used because it contains all the possible parameters for Currencies.
    You can check the documentation of a Currency to see its parameters
    """

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

    # With euro sign
    print(
        EUR(value, currency_symbol=True, eur_sign=True)
    ) # >> "€ 1.250,51"

    # With position
    print(
        EUR(value, currency_symbol=True, eur_sign=True, sign_position="right")
    ) # >> "1.250,51 €"

    # Customized separators:
    print(
        EUR(value, thousands_sep='!!', decimal_sep=';;', decimals=3, currency_symbol=True, eur_sign=True)
    ) # >> "€ 1!!250;;505"


if __name__ == "__main__":
    main(1250.505)