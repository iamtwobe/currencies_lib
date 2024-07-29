from currencies_lib import JPY

def main(value = None):
    # Simple usage:
    print(
        JPY(value)
    ) # >> "1,250.51"

    # With currency symbol:
    print(
        JPY(value, currency_symbol=True)
    ) # >> "¥1,250.51"

    # Customized separators:
    print(
        JPY(
            value, thousands_sep='!!', currency_symbol=True
        )
    ) # >> "¥1!!250;;505"


if __name__ == "__main__":
    main(1250.505)