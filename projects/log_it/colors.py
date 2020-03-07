def print_black(input_string):
    print(input_string)

def print_green(input_string):
    print("\033[92m{}\033[00m" .format(input_string))

def print_red(input_string):
    print("\033[91m{}\033[00m" .format(input_string))


if __name__ == "__main__":
    print('Hello, you are in the colors module. Current available colors are as follows:')
    print('Green, Red')
