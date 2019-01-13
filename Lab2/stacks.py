"""Contains both the StackArray class and the StackLinked class implementations. They both have the same working functions
and take in the same parameters.
"""

class StackArray:
   """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

   def __init__(self, capacity):
      """Creates and empty stack with a capacity"""
      self.capacity = capacity
      self.items = [None]*capacity
      self.num_items = 0
   def __eq__(self, other):
      return (self.items == other.items and self.num_items == other.num_items)


   def check_items(self):
      self.num_items = 0
      for i in range(len(self.items)):
         if(self.items[i]!= None):
            #print(i)
            self.num_items +=1

   def is_empty(self):
      """Returns true if the stack self is empty and false otherwise"""
      StackArray.check_items(self)
      if(self.num_items == 0):
         return True
      else:
         return False
 
   def is_full(self):
      """Returns true if the stack self is full and false otherwise"""
      StackArray.check_items(self)
      #print("number of items: ", self.num_items)
      if(self.capacity == self.num_items):
         return True
      else:
         return False

   def push(self, item):
      if(StackArray.is_full(self)):
         raise IndexError
      else:
        
         #self.items.append(item)
         self.items[self.num_items] = item
         self.num_items+=1
         

   def pop(self):
      """Returns item on the top of the stack and removes it"""
      if(StackArray.is_empty(self)):
         raise IndexError
      else:
         StackArray.check_items(self)
         #print(self.num_items)
         itemremoved = self.items[self.num_items-1]
         self.items[self.num_items-1] = None
         self.num_items-=1
         return itemremoved

   def peek(self):
      """Returns item on the top of the stack but does not remove it"""
      if(StackArray.is_empty(self)):
         raise IndexError
      else:
         StackArray.check_items(self)
         #print(self.num_items)
         return self.items[self.num_items-1]

   def size(self):
      """Returns the number of items in the stack"""
      if(StackArray.is_empty(self)):
         return 0
      else:
         return self.num_items

class Node:
   def __init__ (self, data = None, next = None):
      self.data = data
      self.next = next

   #def __eq__(self, other):
   #   return (self.data == other.data and self.next == other.next)

   def __str__(self):
      return str(self.data)
   
   def get_size(self):
      if(self.next == None):
         return 0
      else: 
         return 1 + self.next.get_size()
      
class StackLinked:

   def __init__ (self, capacity):
      self.capacity = capacity
      self.items = Node(None, None)
      self.num_items = 0


   def is_empty(self):
      """Returns true if the stack self is empty and false otherwise"""

      if(StackLinked.size(self) == 0): 
         return True
      else:
         return False
      
   def is_full(self):
      """Returns true if the stack self is full and false otherwise"""
      size = StackLinked.size(self)
      #print(size)
      if(self.capacity == size):
         return True
      else:
         return False

   def push(self, item):
      if(StackLinked.is_full(self)):
         raise IndexError
      else:
         self.num_items+=1
         self.items = Node(item, self.items)

   def pop(self):
      """Returns item on the top of the stack and removes it"""
      if(StackLinked.is_empty(self)):
         raise IndexError
      else:
         #data = self.items.next.data
         #next = self.items.next.next
         self.num_items-=1
         #self.items = Node(data, next)
         self.items = Node(None, self.items.next.next)

   def peek(self):
      """Returns item on the top of the stack but does not remove it"""
      if(StackLinked.is_empty(self)):
         raise IndexError
      else:
         return self.items.data

   def size(self):
      """Returns the number of items in the stack"""
      return self.items.get_size()




