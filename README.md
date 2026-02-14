# Currencies Formatter
![Python Version](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

The **Currencies Formatter Library** (or currencies lib) is a Python library designed to simplify the formatting of monetary values for various currencies. It supports a wide range of currencies and provides options for custom formatting. Whether you need to display values with currency symbols or abbreviate large numbers, this library offers a straightforward solution.

### Features
- Format monetary values for multiple currencies.
- Custom decimal and symbol options.
- Allows conversion of values to percentage format.
- Utility functions for abbreviating units.

### Installing
You can install this library with:
```bash
$ pip install currencies-lib
```
Supports Python 3.10+


### Example of use

```python
from currencies_lib import BRL

value = 1250.50
result = BRL(value)
print(result)
# >> "R$1.250,50"
```
or
```python
from currencies_lib import *

value = 1250.50
result = format_currency(value, "EUR", spaced=True) # Specify currency code
print(result)
# >> "€ 1.250,50"
```
Additional Examples
```python
# Percentages
print(as_percentage(1000, 25))
# >> 250
print(as_percentage(1000, "25%", subtraction=True))
# >> 750

# Abbreviations
print(unit_abbreviator(1200000))  
# >> "1.2M"
```

### Contributing

I welcome contributions to improve this library! If you have suggestions, bug reports, or new feature requests, please open an issue or submit a pull request on my [GitHub repository](https://github.com/iamtwobe/currencies_lib).

### License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/iamtwobe/currencies_lib/blob/main/LICENSE) file for details.