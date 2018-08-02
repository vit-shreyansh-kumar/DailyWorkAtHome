__about__ = """ Basic memory management in python """

#Although python uses heap memory
#All the names are stored in the memory stack
#De-allocation is done by reference count by the garbage collector

a = 10
b = 10

""" Test now. """
print("A's location:",id(a))
print("B's location:",id(b))

a = 12
print("A's location:",id(a))
print("B's location:",id(b))

b= 20
print("B's Location:",id(b))

""" lists. """

a = [1,2,3,4]
b = a

print("A's location:",id(a))
print("B's location:",id(b))

a.append(5)

print("A's location:",a)
print("B's location:",b)
