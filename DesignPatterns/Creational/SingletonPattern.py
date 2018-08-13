__about__ = """ Implementing singleton design pattern. """

""" Simple implementation of Singleton. """

class Singleton:
    def __new__(cls):

        if hasattr(cls,'instance'):
            return cls.instance

        else:
            cls.instance = super(Singleton,cls).__new__(cls)
            return cls.instance


""" Implementation using metaclasses. """


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":
    a = Logger()
    b = Logger()

    print(a)
    print(b)