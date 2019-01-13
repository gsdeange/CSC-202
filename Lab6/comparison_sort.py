import unittest
import random

"""contains the 3 different types of sorting functions and the test cases for all of them. Each one keeps track of the number
of comparisons and returns them
"""
mergecomparisons = 0

def insert_sort(alist):
   comparisons = 0
   for i in range(len(alist)):
      current = alist[i]
      position = i
      while position > 0 and alist[position-1] > current:
         alist[position] = alist[position-1]
         position-=1
         comparisons +=1
      alist[position] = current
      comparisons +=1
   return comparisons

def select_sort(alist):
   comparisons = 0
   for i in range(len(alist)):
      smallest = i
      for k in range(i+1, len(alist)):
         comparisons+=1
         if alist[k] > alist[smallest]:
            smallest = k

      temp = alist[smallest]
      alist[smallest] = alist[i]
      alist[i] = temp
   return comparisons



def merge_sort(alist):
   if len(alist) > 1:
      #comparisons +=1
      mid = len(alist)//2
      left = alist[:mid]
      right = alist[mid:]
      merge_sort(left)
      merge_sort(right)
      i = 0
      k = 0
      j = 0
      while i < len(left) and j < len(right):
         #comparisons+=1
         if left[i] < right[j]:
            alist[k] = left[i]
            i+=1
         else:
            alist[k] = right[j]
            j+=1
         k = k+1
      while i < len(left):
         #comparisons+=1
         alist[k] = left[i]
         i+=1
         k+=1
      while j < len(right):
         #comparisons+=1
         alist[k] = right[j]
         j+=1
         k+=1


def random_list(size):
      return [random.randrange(1, 10) for _ in range(0, size)]

class Test_Sorts(unittest.TestCase):

   
   
   def test_insert_sort(self):
      test1 = random_list(5)
      test2 = random_list(10)
      test3 = random_list(15)
      test4 = random_list(40)
      test5 = random_list(100)
      test6 = random_list(160)
      test7 = random_list(320)
      test8 = random_list(640)
      
      print("insert sort comparisons:")
      print("giant")
      print("5 , ", insert_sort(test1))
      print("10 , ", insert_sort(test2))
      print("15 , ", insert_sort(test3))
      print("40 , ", insert_sort(test4))
      print("100, ", insert_sort(test5))
      print("160 , ", insert_sort(test6))
      print("320 , ", insert_sort(test7))
      print("640, ", insert_sort(test8))
      

   def test_select_sort(self):
      test1 = random_list(5)
      test2 = random_list(10)
      test3 = random_list(15)
      test4 = random_list(40)
      test5 = random_list(100)
      test6 = random_list(160)
      test7 = random_list(320)
      test8 = random_list(640)
      
      print("select sort comparisons:")
      print("5 , ", select_sort(test1))
      print("10 , ", select_sort(test2))
      print("15 , ", select_sort(test3))
      print("40 , ", select_sort(test4))
      print("100, ", select_sort(test5))
      print("160 , ", select_sort(test6))
      print("320 , ", select_sort(test7))
      print("640, ", select_sort(test8))

   def test_merge_sort(self):
      test1 = random_list(5)
      test2 = random_list(10)
      test3 = random_list(15)
      test4 = random_list(40)
      test5 = random_list(100)
      test6 = random_list(160)
      test7 = random_list(320)
      test8 = random_list(640)
      
      print("merge sort comparisons:")
      print("5 , ", merge_sort(test1))
      print("10 , ", merge_sort(test2))
      print("15 , ", merge_sort(test3))
      print("40 , ", merge_sort(test4))
      print("100, ", merge_sort(test5))
      print("160 , ", merge_sort(test6))
      print("320 , ", merge_sort(test7))
      print("640, ", merge_sort(test8))
      



if __name__ == '__main__':
   unittest.main()