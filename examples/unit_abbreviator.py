from currencies_lib import unit_abbreviator

def main():
    
    # Basic usage:
    print(
        unit_abbreviator(1000) # decimals=1 by default
    ) # >> 1.0k

    print(
        unit_abbreviator(1000, decimals=0)
    ) # >> 1k

    print(
        unit_abbreviator(1000000, decimals=0)
    ) # >> 1M

    print(
        unit_abbreviator(1000000000, decimals=0)
    ) # >> 1B

    print(
        unit_abbreviator(1000000000000, decimals=0)
    ) # >> 1T

    print(
        unit_abbreviator(1255000000, decimals=2)
    ) # >> 1.25B

if __name__ == "__main__":
    main()