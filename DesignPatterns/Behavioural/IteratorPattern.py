__about__ = """ The code implements an iterator pattern. """


class Iterator:

    def __init__(self, stop):
        self.x = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.x < self.stop:
            self.x += 1
            return self.x - 1
    


if __name__ == "__main__":

    itr = Iterator(10)
    for x in itr:
        print(x)

