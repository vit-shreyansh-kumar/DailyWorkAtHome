class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None
        
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.curr = self.head
        
    
    def insert(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.curr = self.head
            
        else:
            temp.prev = self.curr
            self.curr.next = temp
            self.curr = self.curr.next
            
            
    def printdata(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
if __name__ == "__main__":
    
    dd = DoublyLinkedList()
    dd.insert(5)
    dd.insert(6)
    dd.insert(7)
    dd.insert(8)
    dd.insert(9)
    dd.insert(10)
    dd.insert(11)
    dd.insert(12)
    dd.insert(13)
    dd.insert(14)
    
    dd.printdata()
