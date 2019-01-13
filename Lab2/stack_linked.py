class StackLinked:

   def __init__ (self, first, rest):
      self.first = first
      self.rest = rest

   def __eq__(self, other):
      return (type(other) == Pair and self.first == other.first and self.rest == other.rest)

   def is_empty(self):
      """Returns true if the stack self is empty and false otherwise"""
      if(self == None):
         return True
      else:
         return False
      
   def is_full(self):
      """Returns true if the stack self is full and false otherwise"""

      pass

   def push(self, item):
      if(is_full(self)):
         return IndexError
      else:
         return StackLinked(item, self.rest)

   def pop(self):
      """Returns item on the top of the stack and removes it"""
      if(is_empty(self)):
         return IndexError
      else:
         return StackLinked

      pass
   def peek(self):
      """Returns item on the top of the stack but does not remove it"""
      if(is_empty(self)):
         return None
      else:
         return self.first

   def size(self):
      """Returns the number of items in the stack"""
      if(self == None):
         return 0
      else:
         return 1 + size(self.rest)


