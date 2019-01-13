#binary_search_tree.py

class TreeNode:
   def __init__(self, key, data = None, left = None, right= None, parent = None):
      self.key = key
      self.data = data
      self.left = left
      self.right = right
      self.parent = parent

   def __eq__(self, other):
      return self.key == other.key and self.data == other.data and self.left == other.left and self.right == other.right and self.parent == other.parent

   def hasLeftChild(self):
      return self.leftChild

   def hasRightChild(self):
      return self.rightChild

   def isLeftChild(self):
      return self.parent and self.parent.leftChild == self

   def isRightChild(self):
      return self.parent and self.parent.rightChild == self

   def isRoot(self):
      return not self.parent

   def isLeaf(self):
      return not (self.rightChild or self.leftChild)

   def hasAnyChildren(self):
      return self.rightChild or self.leftChild

   def hasBothChildren(self):
      return self.rightChild and self.leftChild

   def replaceNode(self, key, data, left, right):
      self.key = key
      self.data = data
      self.left = left
      self.right = right
      if self.hasLeftChild():
         self.left.parent = self
      if self.hasRightChild():
         self.right.parent = self


   def insert(self, key, data = None):
      #inserts a node with key into the correct position if not a duplicate
      # to check if duplicate, just check the key
      if key < self.key:
         if self.left is None:
            self.left = TreeNode(key, data, parent=self)
         else:
            self.left.insert(key, data)
      elif key > self.key:
         if self.right is None:
            self.right = TreeNode(key, data, parent = self)
         else: 
            self.right.insert(key, data)
      elif key == self.key:
         raise IndexError("duplicate key")
   def spliceOut():
      if self.isLeaf():
         if self.isLeftChild():
            self.parent.left = None
         else:
            self.parent.right = None
      elif self.hasAnyChildren():
         if self.hasLeftChild():
            if self.isLeftChild():
               self.parent.left = self.left
            else:
               self.parent.right = self.left
            self.left.parent = self.parent
         else:
            if self.isLeftChild():
               self.parent.right = self.right
            else:
               self.parent.right = self.right
            self.right.parent = self.parent


   def find_successor(self): 
      #returns the node that is the inorder successor of the node
      successor = None
      if self.hasRightChild():
         successor = self.right.find_min()
      else:
         if self.parent:
            if self.isLeftChild():
               successor = self.parent()
            else:
               self.parent.right = None
               successor = self.parent.find_successor()
               self.parent.right = self


   def find_min(self):                                                                        
      #returns min key in the tree
      current = self
      while current.left.key != None:
         current = current.left
      return current.key
      
   def find_max(self):
      #returns the max key in the tree
      current = self
      while current.key != None:
         current = current.right
      return current.key

   def inorder_print_tree(self):
      #prints inorder the subtree of self
      if(self.left is not None):
         self.left.inorder_print_tree()
      print(self.key)
      if(self.right is not None):
         self.right.inorder_print_tree()

   def print_levels(self):
      #inorder transversal prints the list of pairs [key, level of the node, ] where root is level 0
      if self.get_height() == 0:
         print(self.root.key, "0")
      else:
         if(self.left is not None):
            self.left.print_levels()
         print(self.key, self.get_height())
         if(self.right is not None):
            self.right.print_levels()

   #find which level you are on
   def get_height(self):
      level = 0
      parent = self.parent
      while parent != None:
         level+=1
         parent = parent.parent
      return level

class BinarySearchTree:
   
   def __init__(self):
      self.root = None
      self.size = 0

   def find(self, key):
      #returns true if key is in a node of the tree, else false
      current = self.root
      while current != None and current.key != key:
         if key > current.key:
            current = current.right
         else:
            current = current.left 
      if current is None:
         return False
      else: 
         return True 

   def insert(self, newkey):
      #inserts new Tree Node with newkey, assumes newkey not in tree
      if(self.root is None):
         self.root = TreeNode(newkey)
         self.size +=1
      else: 
         current = self.root
         if(current.key > newkey):
            if(current.left is None):
               current.left = TreeNode(newkey)
               self.size +=1
            else:
               current.left.insert(newkey)
         else:
            if(current.right is None):
               current.right = TreeNode(newkey)
               self.size +=1
            else:
               current.right.insert(newkey)

   def get(self, key, currentnode):
      if not currentnode:
         return None
      elif currentnode.key == key:
         return currentnode
      elif key < currentnode.key:
         return self.get(key, currentnode.left)
      elif key > currentnode.key:
         return self.get(key, currentnode.right)


   def delete(self, key):
      #deletes the node containing key, assuming that the node exists with that key
      if self.size > 1:
         nodeToRemove = self.get(key, self.root)
         if nodeToRemove:
            self.remove(nodeToRemove)
            self.size -=1
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size -=1 


   def remove(self, currentnode):
      if currentnode.isLeaf(): #leaf
         if currentnode == currentnode.parent.left:
               currentnode.parent.left == None
         else:
            currentnode.parent.right = None
      elif currentnode.hasBothChildren(): #interior node
         successor = currentnode.find_successor()
         successor.spliceOut()
         currentnode.key = successor.key
         currentnode.data = successor.data
      else: # node only has one child
         if curretnode.hasLeftChild():
            if currentnode.isLeftChild():
               currentnode.left.parent = currentnode.parent
               currentnode.parent.left = currentnode.left
            elif currentnode.isRightChild():
               currentnode.left.parent = currentnode.parent
               currentnode.parent.right = currentnode.left
            else:
               currentnode.replaceNode(currentnode.left.key, currentnode.left.data, currentnode.left.left, currentnode.left.right)
         else:
            if currentnode.isLeftChild():
               currentnode.right.parent = currentnode.parent
               currentnode.parent.left = currentnode.right
            elif currentnode.isRightChild():
               currentnode.right.parent = currentnode.parent
               currentnode.parent.right = currentnode.right
            else:
               currentnode.replaceNode(currentnode.right.key, currentnode.right.data, currentnode.right.left, currentnode.right.right)

   def print_tree(self):
      #print inorder the entire tree
      if self.is_empty():
         print("empty tree")
      else:
         self.inorder_print_tree()
   
   def is_empty(self):
      #returns true if tree is empty, else false
      return self.size == 0



