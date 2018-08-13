

def main(a,b):

    a = a
    b = b

    shr(a,b)

    print(a)
    print(b)

def shr(a,b):
    a,b = b,a


if __name__ == "__main__":

    main(10,20)
