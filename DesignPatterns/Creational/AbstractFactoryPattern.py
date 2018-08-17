#Abstract Factory Design Pattern.

from abc import ABCMeta , ABC, abstractmethod


class VegPizza(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):

    @abstractmethod
    def serve(self, NonVegPizza):
        pass


class DeluxVegPizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self):
        print("Serve", type(self).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)