__about__="Class method vs Static Method."


class MyClass:
    def method(self):
        print("Instance of method called", self)

    @classmethod
    def classmethod(cls):
        print("Instance of classmethod called", cls)

    @staticmethod
    def staticmethod():
        print("Instance of staticmethod called")

    