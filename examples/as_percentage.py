from currencies_lib import as_percentage

def main(value = None):
    
    # Basic usage:
    print(
        as_percentage(value, percent=25)
    ) # >> 250
    # Returns 25% of the value


    # Percent deduction usage:
    print(
        as_percentage(value, percent=25, subtraction=True)
    ) # >> 750
    # Returns the value reduced by 25%


    # Formatting usage:
    print(
        as_percentage(1256.99, percent=35, # In percent, you can use "35%" instead of just "35"
                       decimals=3, isfloat=False)
    ) # >> 439.947
    # As default, "as_percentage" returns values in float, so you can't specify decimals
    #   so you have to specify "isfloat" as False in order to use decimals


    # More examples:
    _value = 359.90
    print(
        as_percentage(_value, percent=50, subtraction=True, decimals=3, isfloat=False)
    ) # >> 179.950 (359 - 50%)

    print(
        _value - as_percentage(_value, percent="62%")
    ) # >> 136.76 (359 - 62%)

if __name__ == "__main__":
    main(1000)