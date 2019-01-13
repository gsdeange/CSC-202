#heap_lab.py

class MaxHeap:
   def __init__(self, capacity = 50):
      self.capacity = capacity
      self.heapList = [0]*capacity
      self.size = 0
   
   def perc_down(self, i):
      while(i*2) <= self.size:
         mc = self.minChild(i)
         if self.heapList[i] > self.heapList[mc]:
            temp = self.heapList[i]
            self.heapList[i] = self.heapList[mc]
            self.heapList[mc] = temp
         i = mc

   def minChild(self, i):
      if i*2 +1 > self.size:
         return i*2
      else:
         if self.heapList[i*2] < self.heapList[i*2+1]:
            return i*2
         else:
            return i*2+1  

   def perc_up(self, i):
      while i//2 > 0:
         if self.heapList[i] < self.heapList[i//2]:
            temp = self.heapList[i//2]
            self.heapList[i//2] = self.heapList[i]
            self.heapList[i] = temp
         i = i//2

   def insert(self, item):
      self.heapList.append(item)
      self.size+=1
      self.perc_down(self.size)

   def find_max(self):
      maxvalue = self.heapList[1]
      for i in range(len(self.heapList)):
         if(self.heapList[i] > maxvalue):
            maxvalue = self.heapList[i]
      return maxvalue
      

   def del_max(self):
      maxvalue = self.find_max()
      self.heapList[1] = self.heapList[self.size]
      self.size -= 1
      self.perc_up(1)
      return maxvalue
         

   def heap_contents(self):
      return self.heapList[1:]

   def build_heap(self, alist):
      i = len(alist) //2
      self.size = len(alist)
      self.heapList = [0] + alist[:]
      #print(self.heapList)
      while(i>0):
         self.perc_up(i)
         i = i-1

   def is_empty(self):
      return self.size == 0
   def is_full(self):
      return self.size == self.capacity
   def get_heap_cap(self):
      return self.capacity
   def get_heap_size(self):
      return self.size

   def heap_sort_increase(self, alist):
      build_heap(alist)
      while heapList.size > 0:
         maxvalue = self.del_max()
         heapList[self.size+1] = maxvalue
      return self.heapList[1:]

