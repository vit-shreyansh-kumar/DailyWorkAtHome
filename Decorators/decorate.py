__about__ = """ Decorators example. """


def decorate(func):
    def wrap(fname,lname):
        fname = "Fname modified."
        lname = "Lname modified."
        func(fname, lname)
    return wrap

if __name__ == "__main__":

    @decorate
    def mains(fname,lname):
        print(fname)
        print(lname)

    mains("YO","ZO")