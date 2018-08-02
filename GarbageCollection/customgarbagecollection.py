__about__= """Custom garbage collection in python."""

import gc
import pprint

class LinkedList(object):
    def __init__(self, name):
        self.name = name
        self.next = None
    def set_next(self, next):
        print('Linking nodes %s.next = %s' % (self, next))
        self.next = next
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)


if __name__ == "__main__" :
    a = LinkedList('1')
    b = LinkedList('2')
    c = LinkedList('3')
    a.set_next(b)
    b.set_next(c)
    c.set_next(a)

    # Remove references to the LinkedList nodes in this module's namespace
    a = b = c = None

    # Show the effect of garbage collection
    for i in range(2):
        print('Collecting %d ...' % i)
        n = gc.collect()
        print('Unreachable objects:', n)
        print('Remaining Garbage:', pprint.pprint(gc.garbage))
        print