#!python3

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """Returns whether a string is a palindrome or not."""

    assert isinstance(text, str), 'input is not a string: {}'.format(text)

    return is_palindrome_iterative(strip_string(text))
    # return is_palindrome_recursive(strip_string(text))

def strip_string(text):
    """Strip string of anything that is not in the letters category and return all lowercase string."""
    output = ""
    for char in text:
        if char in string.ascii_lowercase or char in string.ascii_uppercase:
            output += char.lower()

    return output

def is_palindrome_iterative(text):
    output = True
    for index, value in enumerate(text):
        if value != text[len(text) - 1 - index] and index < len(text) // 2:
            output = False
            break

    return output


def is_palindrome_recursive(text, left=0, right=None):
    if right is None:
        right = len(text) - 1

    if len(text) % 2 == 0:
        if right - left == -1:
            return True
    else:
        if right - left <= 1:
            return True

    if text[left] != text[right]:
        return False

    return is_palindrome_recursive(text, left + 1, right - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
