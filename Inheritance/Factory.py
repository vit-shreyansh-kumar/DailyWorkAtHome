__about__=""" Factory Design Pattern. """



class ShapeInterface:
    def draw(self):pass

class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")

class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")

class Rectangle(ShapeInterface):
    def draw(self):
        print("Rectangle.draw")

class ShapeFactory:
    @staticmethod
    def getshape(type):
        if type == 'Circle':
            return Circle()
        if type == 'Square':
            return Square()
        if type == 'Rectangle':
            return Rectangle()
        assert 0,"Could not find the shape "+type



if __name__=='__main__':

    f = ShapeFactory()
    s = f.getshape('Rectangle')
    print(s)
