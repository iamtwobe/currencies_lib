from currencies_lib import format_currency

def main():
    
    # Basic usage:
    print(
        format_currency(1000)
    )

    # Specifying the currency symbol:
    print(
        format_currency(1000, currency_symbol="£")
    ) # >> £1,000.00

    # Specifying the sign position:
    print(
        format_currency(1000, currency_symbol=" €", sign_position="right")
    ) # >> 1,000.00 €

    # Separators and decimals:
    print(
        format_currency(1000, currency_symbol="₽ ", sign_position="left",
                        thousands_sep=" ", decimal_sep=",", decimals=3)
    ) # >> ₽ 1 000,000


if __name__ == "__main__":
    main()