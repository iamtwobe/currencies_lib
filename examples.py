from currencies_lib import *

def main():
    value = 21250.956

    # When 'subtraction = True' >> value = initial value - 25% (15938.22)
    # and when False >> value = 25% of initial value (5312.74)
    formated_as_percentage = as_percentage(value, percent=25, isfloat=False, subtraction=False, decimals=2)
    print(formated_as_percentage)

    string_to_float = str_to_float(f'{BRL(value, decimals=2)}')
    print(string_to_float)

    # Rounds values (21250 > 21.3 | 21220 > 21.2k)
    abbreviated_value = unit_abbreviator(value, decimals=1)
    print(abbreviated_value)

    formated_currency_with_sign = format_currency(
        value,
        currency_symbol='P$',
        sign_position='left',
        thousands_sep='.',
        decimal_sep=',',
        decimals=3
    )
    print(formated_currency_with_sign)

    detected_currency = detect_currency(f'{value} C$')
    print('>', detected_currency)

    cutom_formatting = custom_format(
        value, 
        custom_format='_.3f',
        sign_position="right", # if 'left' > "$$ value" elif 'right' > "value $$"
        currency_symbol='$$',
        decimal_sep=';',
        thousands_sep='/'
    )
    print(cutom_formatting)

    usd_format = USD(value, currency_symbol=True, decimals=3)
    print(usd_format)
    
    brl_format = BRL(value, currency_symbol=True, decimals=3)
    print(brl_format)

    eur_format = EUR(value, currency_symbol=True, eur_sign=True, decimals=3)
    print(eur_format)

    rub_format = RUB(value, currency_symbol=True, decimals=3)
    print(rub_format)

    gbp_format = GBP(value, currency_symbol=True, decimals=3)
    print(gbp_format)

    jpy_format = JPY(value, currency_symbol=True)
    print(jpy_format)

    cad_format = CAD(value, currency_symbol=True, decimals=3)
    print(cad_format)

    # This currency has a different value to show the format in bigger numbers
    #   as it has a different currency format (00,00,000.00)
    inr_format = INR(1521250.956, currency_symbol=True, decimals=3)
    print(inr_format)

if __name__ == "__main__":
    main()