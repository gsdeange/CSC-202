import unittest
from heap_lab import *
import random



def random_list(size):
   return [random.randrange(1, 10) for _ in range(0, size)]
#print(random_list(10))


heap1 = MaxHeap()
heap1.build_heap(random_list(10))
#print(heap1.heap_contents())

class Test_Heap_Lab(unittest.TestCase):
   
   def test_insert(self):
      heap2 = MaxHeap()
      heap2.insert(5)
      self.assertListEqual([5], heap2.heapList[-1:])
   def test_find_max(self):
      heap2 = MaxHeap()
      #heap2.insert(5)
      #heap2.insert(7)
      heap2.build_heap([5, 7])
      #print(heap2.heapList)
      self.assertEqual(7, heap2.find_max())
   def test_del_max(self):  
      heap2 = MaxHeap()
      heap2.build_heap([5, 7])
      #self.assertEqual(7, heap2.del_max())
      #self.assertEqual(7, heap2.find_max())
   def test_heap_contents(self):
      heap2 = MaxHeap()
      heap2.build_heap([5, 7])
      heap = heap2.heap_contents()
      self.assertEqual([5, 7], heap[:2])
   def test_build_heap(self):
      heap2 = MaxHeap()
      heap2.build_heap([5, 7])
      self.assertListEqual([5, 7], heap2.heapList[1:3])
   def test_is_empty(self):
      heap3 = MaxHeap()
      self.assertEqual(heap3.is_empty(), True)
   def test_is_full(self):
      heap3 = MaxHeap(5)
      for i in range(5):
         heap3.insert(i)
      self.assertEqual(heap3.is_full(), True)
   def test_get_heap_cap(self):
      heap3 = MaxHeap()
      self.assertEqual(50, heap3.get_heap_cap())
   def test_get_heap_size(self):
      heap3 = MaxHeap(5)
      for i in range(5):
         heap3.insert(i)
      self.assertEqual(heap3.get_heap_size(), 5)
   def test_heap_sort_increase(self):
   	
if __name__ == '__main__':
   unittest.main()