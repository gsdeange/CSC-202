import unittest
import queues

"""This file will test the implementations of both the QueueArray and QueueLinked classes. Both function identically except with
the difference being that one uses arrays and the other linked lists
"""

#test arrays and linked lists
#empty queues
array1 = queues.QueueArray(10)
linked1 = queues.QueueLinked(10)

#full queues
array2 = queues.QueueArray(10)
for i in range(10):
	array2.items[i] = i

linked2 = queues.QueueLinked(10)
for i in range(10):
   queues.QueueLinked.enqueue(linked2, i)
   #print(linked2.size)
	#print(linked2.items)


#test queues
array3 = queues.QueueArray(10)
for i in range(5):
   queues.QueueArray.enqueue(array3, i)

array3enqueued = queues.QueueArray(10)
for i in range(6):
   queues.QueueArray.enqueue(array3enqueued, i)

array4 = queues.QueueArray(10)
for i in range(10):
   queues.QueueArray.enqueue(array4, i)

array4dequeued = queues.QueueArray(10)
for i in range(9):
   queues.QueueArray.enqueue(array4dequeued, i+1)

#test printer
#for i in range(len(array3.items)):
   #print(array3.items[i])
   #print(queues.QueueArray.num_in_queue(array3))


linked3 = queues.QueueLinked(10)
for i in range(5):
   queues.QueueLinked.enqueue(linked3, i)
   #print(linked3.items)

#print("---------")

#for i in range(10):
#  print(linked3.items.data)   

#print("=============")

linked3enqueued = queues.QueueLinked(10)
for i in range(6):
   queues.QueueLinked.enqueue(linked3enqueued, i)
   #print(linked3enqueued.items)

linked4 = queues.QueueLinked(10)
for i in range(10):
   queues.QueueLinked.enqueue(linked4, i)
   #print(linked4.front)
queues.QueueLinked.dequeue(linked4)


#for i in range(10):
#   print(linked4.items)

linked4dequeued = queues.QueueLinked(10)
for i in range(9):
   queues.QueueLinked.enqueue(linked4dequeued, i+1)
   #print(linked4dequeued.items)
#queues.QueueLinked.enqueue(linked4dequeued, None)


#test the functions
class Test_Queues(unittest.TestCase):

   def test_is_empty(self):
   	self.assertTrue(queues.QueueArray.is_empty(array1))
   	self.assertTrue(queues.QueueLinked.is_empty(linked1))

   def test_is_full(self):

   	self.assertFalse(queues.QueueArray.is_full(array1))
   	self.assertFalse(queues.QueueLinked.is_full(linked1))
   	self.assertTrue(queues.QueueArray.is_full(array2))
   	self.assertTrue(queues.QueueLinked.is_full(linked2))
   
   def test_enqueue(self):

      with self.assertRaises(IndexError):
         queues.QueueArray.enqueue(array2, 1)
      with self.assertRaises(IndexError):
         queues.QueueLinked.enqueue(linked2, 1)

      #array implementation
      queues.QueueArray.enqueue(array3, 5)
      self.assertEqual(array3.items, array3enqueued.items)

      #linked list implementation
      queues.QueueLinked.enqueue(linked3, 5)
      for i in range(10):
         self.assertEqual(linked3.front.data, linked3enqueued.front.data)

   def test_dequeue(self):

      with self.assertRaises(IndexError):
         queues.QueueArray.dequeue(array1)
      with self.assertRaises(IndexError):
         queues.QueueLinked.dequeue(linked1)

      #array implementation
      queues.QueueArray.dequeue(array4)
      self.assertEqual(array4.items, array4dequeued.items)

      #linked implementation
      queues.QueueLinked.dequeue(linked4)
      for i in range(10):
         self.assertEqual(linked4.rear.data, linked4dequeued.rear.data)
         #print(linked4.items.data, ".......", linked4dequeued.items.data)

   def test_num_in_queue(self):
      
      self.assertEqual(queues.QueueArray.num_in_queue(array2), 10)
      self.assertEqual(queues.QueueLinked.num_in_queue(linked2), 10)


if __name__ == '__main__':
   unittest.main()