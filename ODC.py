###################################################################################
#######################  ORDERED DICTIONARY IMPLEMENTATION  #######################
###################################################################################
from keyword import iskeyword as _iskeyword
import sys as _sys
import heapq as _heapq
from itertools import repeat as _repeat, chain as _chain, starmap as _starmap


class ODC(dict):
    def __init__(self, *args, **kwargs):

        if len(args) > 1:
            raise TypeError("Expected atmost one argument , got %d arguments", len(args))
        else:
            try:
                self.__root
            except AttributeError:
                self.__root = root = [None,None,None]
                PREV = 0
                NEXT = 1
                root[PREV] = root[NEXT] = root
                self.__map = {}
            self.update(*args,**kwargs)

    def __setitem__(self, key, value, PREV=0, NEXT=1, dict_setitem = dict.__setitem__):
        'Setting a new Item creates a new link which is then set to the end of the linked list'
        if key not in self:
            root = self.__root







