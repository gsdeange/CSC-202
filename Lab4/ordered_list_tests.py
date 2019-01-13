import unittest
import ordered_list

class Test_Ordered_List(unittest.TestCase):
   test1added = ordered_list.OrderedList()
   test1added.add(1)

   def test_add(self):
      test1 = ordered_list.OrderedList()
      test1.add(1)
      test1.add(2)
      self.assertFalse(test1.is_empty())

   def test_remove(self):
      test1 = ordered_list.OrderedList()
      test1.add(1)
      test1.remove(1)
      self.assertTrue(test1.is_empty)

   def test_search_forward(self):
      test1 = ordered_list.OrderedList()
      test1.add(1)
      self.assertTrue(test1.search_forward(1))
	
   def test_search_backward(self):
      test1 = ordered_list.OrderedList()
      test1.add(1)
      self.assertTrue(test1.search_backward(1))

   def test_is_empty(self):
      test1 = ordered_list.OrderedList()
      self.assertTrue(test1.is_empty())

   def test_size(self):
      test1 = ordered_list.OrderedList()
      test1.add(1)
      self.assertEqual(test1.size(), 1)

   def test_index(self):
      test1 = ordered_list.OrderedList()
      test1.add(1)
      self.assertEqual(test1.index(1), 0)

   def test_pop(self):
      test1 = ordered_list.OrderedList()
      test1.add(1)
      test1.pop()
      self.assertTrue(test1.is_empty())

   def test_pop(self):
      test1 = ordered_list.OrderedList()
      test1.add(1)
      test1.pop(0)
      self.assertTrue(test1.is_empty())

if __name__ == '__main__':
   unittest.main()
