#!python3

def factorial(n):
    """Return the product of the integers 1 through n for n >= 0."""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))

    return factorial_iterative(n)
    # return factorial_recursive(n)


def factorial_iterative(n):
    """Iterative implementation of the factorial function."""
    output = 1
    for i in range(2, n + 1):
        output *= i
    return output

def factorial_recursive(n):
    """Recursive implementatin of the factorial function."""
    # check if n is one of the base cases, if it is, return 1
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
