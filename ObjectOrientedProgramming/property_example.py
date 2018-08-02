__about__=""" Adding property to a class."""

class MyObject:
    def __init__(self,name):
        self.name = name

    @property
    def myname(self):

        return self.name

    @myname.setter
    def myname(self):
        return self.name

class Person:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    @property
    def full_name(self):
        return self.fname + " " + self.lname

    @full_name.setter
    def full_name(self,value):
        fname , lname = value.split(" ")
        self.fname = fname
        self.lname = lname

    @full_name.deleter
    def full_name(self):
        del self.fname
        del self.lname

if __name__=="__main__":

    # obj = MyObject("shreyansh")
    # print(obj.myname)
    # obj.myname = "Sinha"

    obj = Person("Shreyansh","Kumar")
    print(obj.fname)
    print(obj.lname)
    print("************************")
    obj.full_name = "Mr Kumar"
    print(obj.fname)
    print(obj.lname)
    print(obj.full_name)