__about__ = "To find the Diameter of the Tree. Code BY Shreyansh."

class Node():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

""" The function is to compute the Height of the
Tree.  
"""

def height(node):
    if node is None:
        return 0
    else:
        return 1+ max(height(node.left), height(node.right))


def diameter(root):

    if root is None:
        return 0

    else:

        lheight = height(root.left)
        rheight = height(root.right)

        ldiameter = diameter(root.left)
        rdiameter = diameter(root.right)

        return max(lheight+rheight+1, max(ldiameter,rdiameter))
