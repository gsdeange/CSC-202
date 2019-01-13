import unittest
import filecmp
from huffman import *

"""contains the testing for the huffman tree functions and the huffman encode and decode functions
"""

class TestList(unittest.TestCase):
   def test_cnt_freq(self):
      freqlist	= cnt_freq("file1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

      freqlist2 = cnt_freq("file2.txt")
      anslist = [0]*256
      anslist[97] = 17
      self.assertEqual(freqlist2[97], anslist[97])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 97)
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 97)
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 100)

      freqlist2 = cnt_freq("file2.txt")
      hufftree2 = create_huff_tree(freqlist2)
      numchars1 = 17
      self.assertEqual(hufftree2.freq, 17)
      self.assertEqual(hufftree2.char, 97)
      


   def test_create_code(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')


   def test_preord(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      #print(tree_preord(hufftree))
      self.assertEqual(tree_preord(hufftree), "00001a1f1b1c1d")

   def test_01_encodefile(self):
      huffman_encode("file1.txt", "output1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))

   def test_01_decodefile(self):
      freqlist = cnt_freq("file1.txt")
      huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))


if __name__ == '__main__': 
   unittest.main()