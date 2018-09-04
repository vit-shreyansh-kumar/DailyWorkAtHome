def power(x, y):
    """ Initialize the result because x pow 0 = 1 , so this is the base condition."""
    result = 1

    while y > 0:
        """ Check weather y is an odd number. """
        """ If y is odd number then multiply only once starting from the base condition. """
        # x with result
        if (y & 1) == 1:
            result = result * x

        """ If Y is an even number then divide by 2 """
        y = y >> 1
        x = x * x

    return result


if __name__ == "__main__":
    print("Power is ", power(5, 2))