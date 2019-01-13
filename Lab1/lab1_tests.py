import unittest
import lab1
class test_functions(unittest.TestCase):

   def test_max_list_iter(self):
      tlist1 = [0, 1, 2, 3, 4, 5]
      self.assertEqual(lab1.max_list_iter(tlist1), 5)
      tlist2 = [5, 4, 3, 2, 1, 0]
      self.assertEqual(lab1.max_list_iter(tlist2), 5)
      tlist3 = [3, 5, 6, 8, 2, 9]
      self.assertEqual(lab1.max_list_iter(tlist3), 9)
      tlist4 = [1, 1, 1, 1, 1, 1]
      self.assertEqual(lab1.max_list_iter(tlist4), 1)
      tlist5 = [9, 0, 0, 0, 0, 10]
      self.assertEqual(lab1.max_list_iter(tlist5), 10)
      tlist6 = []
      with self.assertRaises(ValueError):
         lab1.max_list_iter(tlist6)
      tlist7 = [-1, -5, -8, -2, -10]
      self.assertEqual(lab1.max_list_iter(tlist7), -2)
      tlist8 = [-1, -1, -1, -1, -1]
      self.assertEqual(lab1.max_list_iter(tlist8), -1)

   def test_reverse_rec(self):
      tempstr1 = 'hello'
      self.assertEqual(lab1.reverse_rec(tempstr1), 'olleh')
      tempstr2 = 'aaaaaa'
      self.assertEqual(lab1.reverse_rec(tempstr2), 'aaaaaa')
      tempstr3 = 'aaaba'
      self.assertEqual(lab1.reverse_rec(tempstr3), 'abaaa')
      

   def test_bin_search(self):
      list_val1 = [1, 2, 3, 4]
      self.assertEqual(lab1.bin_search(3, 0, 3, list_val1), 2)
      list_val2 = [8, 8, 7, 4, 8, 2, 3]
      self.assertEqual(lab1.bin_search(4, 2, 6, list_val2), 1)
      self.assertEqual(lab1.bin_search(8, 2, 6, list_val2), 2)
      self.assertEqual(lab1.bin_search(8, 0, 6, list_val2), 0)
      list_val3 = []
      with self.assertRaises(ValueError):
         lab1.bin_search(4, 0, 6, list_val3)

if __name__ == '__main__':
   unittest.main()