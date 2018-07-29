__about__ = """Merge Sorted Linked List only single traverse allowed."""

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def push(self,value):
        push_node = Node(value)

        if self.head is None:
            self.head = push_node
            self.current = self.head

        else:
            self.current.next = push_node
            self.current = push_node

# def merge(self,head1,head2):
#     temp = None
#
#     if head1 is None:
#         temp = head2
#
#     elif head2 is None:
#         temp = head1
#
#
#     if head1.data <= head2.data:
#
#         temp = head1
#
#         temp.next = self.merge(head1.next,head2)
#
#     else:
#
#         temp = head2
#
#         temp.next = self.merge(head1,head2.next)
#
#     return temp


if __name__ =="__main__":

    l1 = LinkedList()
    l1.push(4)
    l1.push(6)
    l1.push(7)
    l1.push(9)
    l1.push(12)
    l1.push(14)
    l1.push(24)

    # l2 = LinkedList()
    # l2.push(1)
    # l2.push(2)
    # l2.push(3)
    # l2.push(5)
    # l2.push(8)
    # l2.push(10)
    # l2.push(18)
    # l2.push(35)

    # l3 = LinkedList()
    # merged_list = l3.merge(l1,l2)

    tmp = l1
    print("NEW LIST IS:")
    while tmp.next:
        print(tmp.data)
        tmp = tmp.Next




