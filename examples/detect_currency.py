from currencies_lib import detect_currency

def main():

    # Usage:
    print(
        detect_currency('EUR 1.000,00')
    ) # >> EUR

    print(
        detect_currency('1.000, 00 $$')
    ) # >> EUR

    print(
        detect_currency('1.000, 00aC$b')
    ) # >> CAD

if __name__ == "__main__":
    main()