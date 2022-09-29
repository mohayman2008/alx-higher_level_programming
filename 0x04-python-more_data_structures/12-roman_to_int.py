#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
              'M': 1000}
    next_digits = {'I': 'VX', 'X': 'LC', 'C': 'DM'}
    num = 0
    i = 0
    while i < len(roman_string):
        digit = roman_string[i]
        if digit not in digits.keys():
            return None

        if digit not in next_digits.keys() or i >= (len(roman_string) - 1):
            num += digits.get(digit)

        elif (roman_string[i + 1] == digit or
              roman_string[i + 1] not in next_digits[digit]):

            num += digits.get(digit)
            while i < len(roman_string) - 1 and roman_string[i + 1] == digit:
                num += digits.get(digit)
                i += 1
        else:
            num -= digits.get(digit)
        i += 1
    return num


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
