__about__ = "Singly Linked List"

class Node:
    """" Function to initialize the Node object"""
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    """ Initialize the head pointer"""
    def __init__(self):
        self.head = None
        self.current = None

    """ Push to the Linked List"""
    def add(self,data=None):
        if self.head is None:
            self.head = Node(data)
            self.current = self.head

        else:
            new_node = Node(data)
            self.current.next = new_node
            self.current = new_node

    def print_elements(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete(self,data=None,position = None):

        if self.head is None:
            return self.head
        elif position == 0:
            return head.next
            temp = self.head
            test = self.head
            before = self.head
            while temp:
                if temp.data == data:
                    temp = temp.next
                else:
                    temp = temp.next



if __name__ == '__main__':

    ll = LinkedList()
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.add(1)

    ll.print_elements()




