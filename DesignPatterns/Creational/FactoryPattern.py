# Factory Design Pattern.


class Car(object):
    pass


class Bike(object):
    pass


def factory_method(type):

    if type:
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            raise ValueError("Object cannot be created")

