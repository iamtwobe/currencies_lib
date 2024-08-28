from currencies_lib import detect_currency, str_to_float, USD


"""
    Available currencies for detection:
    USD | BRL | EUR | RUB | GBP |
    JPY | CAD | INR
"""

def main():

    # Usage:
    print(
        detect_currency('EUR 1.000,00')
    ) # >> EUR

    print(
        detect_currency('1.000, 00 $$')
    ) # >> USD

    print(
        detect_currency('1.000, 00aC$b')
    ) # >> CAD

    # A good use of the command:
    print(
        globals()[detect_currency('USD 1000')](1000, currency_symbol=True)
    ) # >> $ 1,000.00
    # Detects the currency and formats using USD() method

    _value = 'USD 1.257,994'
    print(
        globals()[detect_currency(_value)](str_to_float(_value), currency_symbol=True, decimals=3)
    ) # >> $ 1,257.994
    # The same as above, but with the original value being inputted again and being treated by str_to_float() method

if __name__ == "__main__":
    main()