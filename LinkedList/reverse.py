__about__ = """ Reverse a linked list. """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = None

    def insert(self,value):

        if self.head is None:
            self.head = Node(value)
            self.curr = self.head

        else:
            temp = Node(value)
            self.curr.next = temp
            self.curr = self.curr.next

    def reverse(self):
        if self.head is None:
            return None
        else:
            prev = None
            curr = self.head

            while curr:

                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.insert(8)

    ll.display()

    ll.reverse()

    ll.display()