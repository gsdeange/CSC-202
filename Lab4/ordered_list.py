class Node:
   def __init__(self, data = None):
      self.data = data
      self.next = None
      self.previous = None

class OrderedList():

   def __init__(self):
      self.head = None
      self.tail = None
      self.num_items = 0

   def add(self, item):
      self.num_items +=1
      new = Node(item)
      if self.head is None:
         self.head = new
      elif self.head.data > new.data:
         new.next = self.head
         self.head.previous = new
         self.head = new
      else:
         prev = self.head
         cur = self.head.next
         while cur is not None:
            if cur.data > new.data:
               prev.set_next(new)
               new.set_prev(prev)
               new.set_next(cur)
               cur.set_prev(new)
               return new
            prev = cur
            cur = cur.next
         prev.set_next(new)
         new.set_prev(prev)
         
         return new

   def remove(self, item):
      temp = self.head
      while(temp is not None):
         if(temp.data == item):
            if(temp.previous is not None):
               temp.previous.next = temp.next
               temp.next.previous = temp.previous
            else:
               self.head = temp.next
               temp.previous = None
         temp = temp.next
      self.num_items-=1

   def search_forward(self, item):
      temp = self.head
      while temp is not None:
         if(temp.data == item):
            return True
         elif temp.data > item:
            return False
         temp = temp.next
      return False

	
   def search_backward(self, item):
      temp = self.tail
      while temp is not None:
         if(temp.data == item):
            return True
         elif(temp.data < item):
            return False
         temp = temp.previous
      return False

   def is_empty(self):
      return self.head is None
  
   def size(self):
      return self.num_items

   def index(self, item):
      index = 0
      current = self.head
      while current is not None:
         if current.data == item:
            return index
         index += 1
         current = current.next
      return index

   def pop(self):
      return self.head

   def pop(self, pos):
      if(self.is_empty()):
         raise ValueError
      previous = self.head
      current = previous.next
      if pos is None:
         while current is not None:
            if current.next is None:
               previous.next = None
               return current
            previous = current
            current = current.next
         self.head = None
         return previous

      if pos == 0:
         self.head = current
         return previous

      cur_index = 0
      while current is not None:
         if cur_index == pos - 1:
            try:
               previous.next = current.next
               current.next = previous
            except:
              previous.next = None
            return current
         previous = current
         current = current.next
         cur_index += 1

