#!/usr/bin/env python3

import string

# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

def decode(digits, base):
    """Decode given digits in given base to number in base 10."""

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    if '.' in digits:
        whole_out = decode_digits(digits.split('.')[0], base)
        frac_out = decode_digits(digits.split('.')[1], base)

        return f'{whole_out}.{frac_out}'
    else:
        return decode_digits(digits, base)


def decode_digits(digits, base):
    output = 0
    index = 0
    for digit in digits:
        if digit not in string.digits:
            digit = convert_char_to_num(digit)

        output += int(digit) * (base**(len(digits) - 1 - index))
        index += 1

    return output

def encode(number, base):
    """Encode given number in base 10 to digits in given base."""

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert float(number) >= 0.0, 'number is negative: {}'.format(number)

    if float(number) == 0.0:
        return "0"

    if '.' in number:
        whole_out = encode_number(number.split('.')[0], base)
        frac_out = encode_number(number.split('.')[1], base)

        return f'{whole_out}.{frac_out}'
    else:
        return encode_number(number, base)

def encode_number(number, base):
    number = int(number)
    encoded_num = ""
    while number != 0:
        remainder = int(number % base)
        remainder_as_char = str(remainder)

        if remainder > 9:
            remainder_as_char = convert_num_to_char(remainder).lower()

        number = int(number // base)
        encoded_num = "{}{}".format(remainder_as_char, encoded_num)

    return encoded_num

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2."""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(digits, base1), base2)


def convert_char_to_num(input_char):
    ascii_keyval = 65
    return int(ord(input_char.upper()) - ascii_keyval) + 10

def convert_num_to_char(input_num):
    ascii_keyval = 65
    return chr((input_num - 10 + ascii_keyval))


def main_convert():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

def main_decode():
    import sys
    args = sys.argv[1:]

    digits = args[0]
    base = int(args[1])

    result = decode(digits, base)

    print("{} in base {} is {} in base 10!".format(digits, base, result))

def main_encode():
    import sys
    args = sys.argv[1:]

    number = args[0]
    base = int(args[1])

    result = encode(number, base)

    print("{} in base 10 is {} in base {}!".format(number, result, base))


if __name__ == '__main__':
    main_convert()
