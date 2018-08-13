

def my_func():
    message = "test"
    def inner_func():
        print(message)

    return inner_func

a = my_func()
b = my_func()

print(a())
print(b())
