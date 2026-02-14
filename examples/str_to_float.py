from currencies_lib import str_to_float

def main(value):

    # Usage:
    print(
        str_to_float(value)
    ) # >> "1250.516"

    # Negative results:
    print(
        str_to_float('$ -1, 250.516  ')
    ) # >> "-1250.516"

    # WARNING:
    # It stops trying to figure if it's a negative when it finds a valid number (0-9)
    # So if the value is "1-1,250.516", it's gonna return "11250.516".

if __name__ == "__main__":
    main('$ 1,250.516  ')