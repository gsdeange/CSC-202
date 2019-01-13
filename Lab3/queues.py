""" Contains the QueueArray and QueueLinked classes that hold implementations of all the same functions, acting as a queue. 
There is also the node class which is used in the QueueLinked class to create a linked list.
"""
class QueueArray:
   def __init__(self, capacity):
      self.capacity = capacity # the maximum number of items that can be stored in queue
      self.size = 0
      self.items = [None]*capacity

   def __eq__(self, other):
      return (self.items == other.items and self.size == other.size)
      
   def is_empty(self):

      if(QueueArray.num_in_queue(self) == 0):
         return True
      else:
         return False
      
   def is_full(self):
      if(QueueArray.num_in_queue(self) == self.capacity):
         return True
      else:
         return False

   def enqueue(self, item):
      # elements are added to the end of the queue
      if(self.is_full()):
         raise IndexError
      else:
         
         self.items[self.size] = item
         #self.num_in_queue = (self.num_in_queue+1)%self.capacity
         self.size +=1
      
   def dequeue(self):
      # elements are removed from the front of the queue
      if(self.is_empty()):
         raise IndexError
      else:
         self.items = self.items[1:]
         self.items.append(None)
         #if(self.num_in_queue != 0):
         #   self.num_in_queue -=1
         #else:
         #   self.num_in_queue
         self.size-=1

     
   def num_in_queue(self):
      '''returns the number of items in the queue'''
      self.size = 0
      for i in range(len(self.items)):
         if(self.items[i] != None):
            self.size +=1
      return self.size


class Node:
   def __init__(self, data = None, next = None):
      self.data = data
      self.next = next
   def __str__(self):
      return str(self.data)

   def get_size(self):
      #returns size of the linked list
      if(self.next == None):
         return 0
      else: 
         return 1 + self.next.get_size()


class QueueLinked:
   def __init__(self, capacity):
      self.capacity = capacity # the maximum number of items that can be stored in queue
      self.size = 0
      self.front = None
      self.rear = None

   def is_empty(self):
      size = QueueLinked.num_in_queue(self)
      if(self.size == 0):
         return True
      else:
         return False
   
   def is_full(self):
      size = QueueLinked.num_in_queue(self)
      if(self.size == self.capacity):
         return True
      else: 
         return False

   def enqueue(self, item):
      #elements are added to the end of the queue
      if(self.is_full()):
         raise IndexError
      elif(self.is_empty()):
         temp = Node(item, None)
         self.front = temp
         self.rear = temp
         self.size+=1
      else:
         self.size = self.size+1
         #print(self.size)
         #print(self.items.data)
         #self.items = Node(item, self.items)
         temp = Node(item)
         self.rear.next = temp
         self.rear = temp

   def dequeue(self):
      #elements are removed from the front of the queue
      if(self.is_empty()):
         raise IndexError
      else:
         returndata = self.front.data
         self.front = self.front.next
         



         #current = self.items
         #previous = None
         #while(current.next != None):
         #   previous = current.data
         #   current = current.next
         #previous = None
         self.size -=1
 
         #self.enqueue(None)

   def num_in_queue(self):
      #"""returns the number of items in the queue"""
      #self.size = self.items.get_size()
      
      #if(self.front.next == None):
      #   return 0
      #else: 
      #   return 1 + get_size(self.front.next)"""

      return self.size