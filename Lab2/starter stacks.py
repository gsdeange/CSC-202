class StackArray:
   """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

   def __init__(self, capacity):
      """Creates and empty stack with a capacity"""
      self.capacity = capacity
      self.items = [None]*capacity
      self.num_items = 0

   def check_items(self):
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
      if(is_full(self)):
         return IndexError
      else:
         self.items.append(item)
         self.num_items+=1

   def pop(self):
      """Returns item on the top of the stack and removes it"""
      if(is_empty(self)):
         return IndexError
      else:
         itemremoved = self.items[-1]
         self.items.remove(self.items[-1])
         self.num_items-=1
         return itemremoved

   def peek(self):
      """Returns item on the top of the stack but does not remove it"""
      if(is_empty(self)):
         return IndexError
      else:
         return self.items[-1]

   def size(self):
      """Returns the number of items in the stack"""
      if(is_empty(self)):
         return 0
      else:
         return self.num_items

class Node:
   def __init__ (self,first, rest = None):
      self.first = first
      self.rest = rest
      #self.capacity = capacity
      #self.num_items = 0
      
class StackLinked:

   """def __init__ (self, capacity, first = None, rest = None ):
      self.first = first
      self.rest = rest
      self.capacity = capacity
      self.num_items = 0"""
      
   def __init__(self, capacity, items):
      self.capacity = capacity
      self.num_items = 0
      self.items = items


   def is_empty(self):
      """Returns true if the stack self is empty and false otherwise"""
      if(self.num_items == 0):
         return True
      else:
         return False
      
   def is_full(self):
      """Returns true if the stack self is full and false otherwise"""
      size = StackLinked.size(self)
      print(size)
      if(self.capacity == size):
         return True
      else:
         return False

   def push(self, item):
      if(is_full(self)):
         return IndexError
      else:
         self.num_items+=1
         return StackLinked(item, StackLinked(self.first, self.rest))

   def pop(self):
      """Returns item on the top of the stack and removes it"""
      if(is_empty(self)):
         return IndexError
      else:
         data = self.rest.first
         next = self.rest.rest
         self.num_items-=1
         return StackLinked(data, next)

   def peek(self):
      """Returns item on the top of the stack but does not remove it"""
      if(is_empty(self)):
         return None
      else:
         return self.first

   def size(self):
      """Returns the number of items in the stack"""
      if(self.rest == None):
         return 0
      else:
         return 1 + StackLinked.size(self.rest)



