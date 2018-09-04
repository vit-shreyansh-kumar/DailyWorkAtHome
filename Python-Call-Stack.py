def foo():
    print("foo line 1")
    print("foo line 2")
    print("foo line 3")


def fum():
    print("fum line 1")
    print("fum line 2")
    print("fum line 3")


def bar():
    print("bar line 1")
    fum()
    foo()
    print("bar line 4")


def go():
    bar()

go()