""" Abstract class implementation. """
from abc import ABC , abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def done_work(self):
        pass


if __name__ == "__main__":
    try:
        a = AbstractClass()
        print(a)

    except Exception as e:
        print("EXCEPTION:",e)