__about__ = "User defined exceptions."


class NoValueException(Exception):
    """ Raised when no value found."""
    pass


class LargeValueException(Exception):
    """ Raised when the value is very large."""
    pass


if __name__ == "__main__":
    i = None
    j = 100000

    try:
        if i is None:
            raise NoValueException


    except NoValueException:
        print("The value is not found.")


    try:
        if j >= 999:
            raise LargeValueException

    except LargeValueException:
        print("The value found is too large.")