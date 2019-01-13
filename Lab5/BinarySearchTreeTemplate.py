# final version for class notes

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, newkey, data=None):

        if self.root is None:			 # if tree is empty
            self.root = TreeNode(newkey, data)
        else:
            p = self.root
            if p.key > newkey:
                if p.left is None:      # no left child from root
                    p.left = TreeNode(newkey, data, parent=p)
                else:
                    p.left.insert(newkey, data)   # call insert of TreeNode on left child
            else:
                if p.right is None:     # no right child from root
                    p.right = TreeNode(newkey, data, parent=p)
                else:
                    p.right.insert(newkey, data)  # call insert of TreeNode on right child

    def find (self, key):   # iterative find method
        p = self.root      # current node
        while p is not None and p.key != key :
            if key < p.key:
                p = p.left
            else:
                p = p.right

        if p is None :  # didn't find key
            return False	    
        else:
            return True     # might want to return the node or ???

    def print_tree(self):
        if self.root == None:
            print()
        else:
            self.root.inorder_print_tree()

class TreeNode:
    """Tree node: key and data + left child, right child, parent"""

    def __init__(self,key,data=None,left=None,right=None,parent=None):

        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, key, data):
        """  Insert new node with key, assumes key not present """
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key, data, parent=self)
            else:
                self.left.insert(key, data)
        elif key > self.key:
            if self.right is None:
                self.right = TreeNode(key, data, parent=self)
            else:
                self.right.insert(key, data)

    def inorder_print_tree(self):
        """   Print tree content inorder        """
        if (self.left != None):
            self.left.inorder_print_tree()
        self.print_node()
        if (self.right != None):
            self.right.inorder_print_tree()

    def print_node(self):
        """   Print Node information """
        if self.parent != None:
            print("key =", self.key, ", data =", self.data, ", parent key: ", self.parent.key)
        else:
            print("key =", self.key, ", data =", self.data, ", root")

t = BinarySearchTree()
t.insert(8, 'hello')
t.insert(3, 'dog')
t.insert(10)
t.insert(1)
print ("Tree after inserting 8, 3, 10, 1")
t.root.inorder_print_tree()
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(14)
t.insert(13)
print ("Tree after inserting 6, 4, 7, 14, 13")
t.print_tree()
print("Testing find 14")
print(t.find(14))
print("Testing find 15")
print(t.find(15))
