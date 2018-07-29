__about__="""find Loop in a Linked list."""

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkeList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        curr = self.head
        if self.head is None:
            self.head = Node(value)
            self.curr = self.head
        else:
            self.curr.next = Node(value)
            self.curr = self.curr.next


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse_list(self):
        prev = None
        current= self.head
        next = current.next

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def remove_duplicate(self):
        temp = self.head
        val = {}
        while temp:
            if temp.data not in val:
                pass
            temp = temp.next

if __name__ == "__main__":
    ll = LinkeList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.insert(8)
    ll.insert(9)
    print("==============================")
    ll.print_list()
    print("==============================")
    ll.reverse_list()
    print("==========REVERSED============")
    ll.print_list()
    print("==============================")