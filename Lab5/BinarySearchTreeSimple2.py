""" simple example of BST from 
    https://www.laurentluce.com/posts/binary-search-tree-library-in-python/comment-page-1/ """

class Node:
    """Tree node: left and right child + data which can be any object"""

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """  Insert new node with data, assumes data not present """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                   self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):

        """   Print tree content inorder        """

        if (self.left != None):
            self.left.print_tree()
        print(self.data)
        if (self.right != None):
            self.right.print_tree()


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
print ("Tree after inserting 8, 3, 10, 1")
root.print_tree()
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
print ("Tree after inserting 6, 4, 7, 14, 13")
root.print_tree()
