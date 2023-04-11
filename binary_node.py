"""
    This file contains the definition of a class to represent nodes of a Binary Tree
"""
class BinaryNode():
    """
     Objects of this class contains an atributte value of any type,
     and atributes left_child, righ_child and parent, also of type BinaryNode.
     It represent a node of a Binary Tree.
    """
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def set_left_child(self, child):
        """
        Set the left child of the current node
        """
        self.left_child = child
        child.parent = self

    def set_right_child(self, child):
        """
        Set the right child of the current node
        """
        self.right_child = child
        child.parent = self
