__about__ = """ Binary Tree Algorithm Python. """

class Node:
    def __init__(self, data = None):
        self.value = data
        self.left = None
        self.right= None

class Tree:

    def __init__(self):
        self.root = None

    #Search a node in the Binary Tree.
    def search(self):


    # Insert Node

    def insert(self,root,node):
        if root is None:
            root = node
        else:
            if root.value < node.value:
