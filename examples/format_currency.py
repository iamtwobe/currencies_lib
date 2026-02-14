from currencies_lib import format_currency

def main():
    
    # Basic usage:
    print(
        format_currency(1000, "EUR")
    ) # >> €1.000,00

    # Specifying the sign position:
    print(
        format_currency(1000, "EUR", symbol_position="right", spaced=True)
    ) # >> 1.000,00 €

    # Separators and decimals:
    print(
        format_currency(1000, "EUR", thousands_sep=",", decimal_sep=".", decimals=3)
    ) # >> €1,000.000


if __name__ == "__main__":
    main()