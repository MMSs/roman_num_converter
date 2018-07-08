# -*- coding: utf-8 -*-

import sys


def toroman(num):
    """
    Convert a decimal number to roman string
    :param num: Number to convert
    :type num: int
    :return: The roman representation
    :rtype: string
    """

    # validate passed argument
    if not isinstance(num, int):
        raise ValueError("Not an intger")

    num_map = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    if len(str(num)) > max([len(str(i)) for i in num_map.keys()]):
        raise ValueError("Number is too big")
    roman = ""
    while num:
        for i, n in enumerate(reversed(str(num))):
            n = int(n)
            if n * 10 ** i in num_map.keys():
                # Number has equivalent roman symbol
                roman = (num_map[n * 10 ** i]) + roman
            elif n < 5:
                # Number doesn't have equivalent roman symbol, so repeat it
                roman = (num_map[10 ** i] * n) + roman
            elif n > 5:
                # Number doesn't have equivalent roman symbol, so repeat it after 5 equivalent symbol
                roman = (num_map[5 * 10 ** i] + (num_map[10 ** i] * (n - 5))) + roman
            num -= n * 10 ** i
    return roman


def fromroman(roman):
    """
    Convert a roman string into integer
    :param roman: The roman number
    :type roman: str
    :return: The integer presentation
    :rtype: int
    """

    # Roman to decimal numerals map
    num_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    roman = roman.upper()
    # Validate number
    for r in roman:
        # Validate each character for being a valid roman symbol
        if r not in num_map.keys():
            raise ValueError("Not a roman numeral")

    # Replace roman symbols with integers
    nums = []
    while roman:
        if roman[0:2] in num_map.keys():
            nums.append(num_map[roman[0:2]])
            roman = roman[2:]
        else:
            nums.append(num_map[roman[0]])
            roman = roman[1:]

    # Validate numerals order
    # Roman numerals order left to right is always greater to smaller
    for i, n1 in enumerate(nums):
        for n2 in nums[i+1:]:
            if n1 < n2:
                # Error if left is smaller than right
                raise ValueError("Invalid roman numeral")
            if n1 + n2 in num_map.values():
                # Error for numeral double representation
                # i.e. IVI for V  or  VV for X
                raise ValueError("Invalid roman numeral")
            if n1 / n2 < 2 and str(n1)[0] in ['4', '9']:
                # Error for wrong subtractive numeral order
                # If left number is less than double the right number and in the group of 4s and 9s
                # i.e. IXV as XIV  or  XCL as CXL
                raise ValueError("Invalid roman numeral")
        if len(nums) > i+4 and nums[i] == nums[i+4]:
            # Prevent repeatition for more than 4 times
            raise ValueError("Invalid roman numeral")

    return sum(nums)


if __name__ == "__main__":
    try:
        num = sys.argv[1]
        if u"{}".format(num).isnumeric():
            print(toroman(int(num)))
        else:
            print(str(fromroman(str(num))))
    except ValueError as err:
        print(err.message)
    except IndexError as err:
        print("Argument is missing")
