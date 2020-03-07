from datetime import datetime
from . import colors

# Types of logs
INFO = 'Info'
SUCCESS = 'Success'
ERROR = 'Error'

# Dict to color functions
type_dict = {
    'Info': colors.print_black,
    'Success': colors.print_green,
    'Error': colors.print_red
}


def log(input, log_type=INFO):
    """Function responsible for logging."""

    date = datetime.now().strftime("%H:%M:%S")
    out = f'{date} || {log_type} || {input}'

    type_dict[log_type](out)


if __name__ == "__main__":
    print("Welcome to logit!")
    print("Usage: logit.log('some text', log_type)")
    print("Available LogTypes: [Info, Warning, Error]")

    info = "Hello this is info"
    success = "Hello this is a warning"
    error = "Hello this is error"

    log(info, INFO)
    log(success, SUCCESS)
    log(error, ERROR)
