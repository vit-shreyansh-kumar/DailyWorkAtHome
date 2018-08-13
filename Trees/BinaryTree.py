__about__ = """ Binary Tree Algorithm Python. """

class Node:
    def __init__(self, data = None):
        self.value = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    #Search a node in the Binary Tree.
    def search(self,data,node):
        if node:
            if node.value == data:
                print("Value found",node.value)
                return
            elif data > node.value:
                print("RIGHT:")
                self.search(data,node.right)
            else:
                print("LEFT:")
                self.search(data,node.left)


    def insert(self, data, curr=None):
        try:
            if curr is None:
                curr = self.root

            if not self.root:
                self.root = Node(data)
            else:
                if curr is not None:
                    if curr.value < data:
                        if curr.right is None:
                            curr.right = Node(data)
                        else:
                            self.insert(data, curr.right)
                    else:
                        if curr.left is None:
                            curr.left = Node(data)
                        else:
                            self.insert(data, curr.left)
                else:
                    print("Current node not found.")
        except Exception as e:
            print("Insertion Error:",e)
        return self.root

    def preorder(self,root):
        # First recur on left child
        if root:
            self.preorder(root.left)
        # then print the data of node
            print(root.value)
        # now recur on right child
            self.preorder(root.right)


if __name__ == "__main__":

    tree = Tree()
    bt = tree.insert(5)
    print("BC:",bt)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(3)
    tree.insert(2)
    tree.insert(11)
    tree.insert(22)
    tree.insert(16)

    # print "Preorder traversal of binary tree is"
    print("**************************************")
    print("LEFT:",bt.left)
    print("RIGHT:",bt.right)
    print("DATA:",bt.value)
    tree.preorder(bt)

    tree.search(2,bt)