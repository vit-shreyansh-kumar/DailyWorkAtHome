__about__ = "Maximum no in a binary tree."

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

class Tree:
    @staticmethod
    def insert(root = None,data = None):
        if root is None and data is not None:
            root = Node(data)
