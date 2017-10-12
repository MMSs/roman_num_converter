# Roman Numeral Converter in Python

This module implements two functions for conveting numerals between the two numeric systems, the roman and the decimal.

## Usage
For usage within an app, it can be installed then import `convert_toroman` and/or `convert_fromroman`:
```python
from roman_converter import toroman, fromroman

toroman(4999)
fromroman('MMMMCMXCIX')
```

Standalone python file execution is also possible, and numbers can be passed as command line arguments.  From within the module directory:
```cli
$ python roman_converter.py 499
> CDXCIX
$ python roman_converter.py CDXCIX
> 499
```
