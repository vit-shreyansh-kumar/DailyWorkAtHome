__about__ = """ Reverse a linked list using tail-end approach. """

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = self.head

    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.curr = self.head

        else:
            temp = Node(data)
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

    def reverse(self,curr,prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        else:

            next = curr.next
            curr.next = prev

            self.reverse(next,curr)

    def doreverse(self):
        if self.head is None:
            return
        else:
            self.reverse(self.head,None)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()
    x = 10
    for i in range(0,10):
        ll.insert(x+i)

    ll.display()
    print("========================================")
    ll.doreverse()
    print("========================================")
    ll.display()