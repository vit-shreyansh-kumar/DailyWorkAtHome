__about__ = """ Decorators example. """


def hello_decorator(func):
    def inner1(a,b):
        # getting the returned value
        a = 10
        b = 22
        returned_value = func(a,b)
        # returning the value to the original frame
        return returned_value
    return inner1

# adding decorator to the function
@hello_decorator
def add_two_numbers(a, b):
    print("Inside the function")
    print("Modified a =", a)
    print("Modified b =", b)
    return a+b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", add_two_numbers(a, b))


# ---Output---
# before Execution
# Inside the function
# Modified a = 10
# Modified b = 22
# after Execution
# Sum = 32
