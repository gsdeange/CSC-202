import unittest
import stacks

"""Tests all of the functions for both the StackArray class and the StackLinked class. In the beginning I create test arrays and
and test linked lists that will demonstrate the working functions. Both of the implementations take in the exact same parameters
so there are no differences when initializing the classes. They work as if they were the same implementations
"""

#test arrays and linked lists
#empty stacks
array1 = stacks.StackArray(10)
linked1 = stacks.StackLinked(10)

#full stacks
array2 = stacks.StackArray(10)
for i in range(10):
	array2.items[i] = i

linked2 = stacks.StackLinked(10)
for i in range(10):
	stacks.StackLinked.push(linked2, i)
	#print(linked2.items)

#array test stacks
array3 = stacks.StackArray(10)
for i in range(5):
	array3.items[i] = i
array3pushed = stacks.StackArray(10)
for i in range(6):
	array3pushed.items[i] = i

array4 = stacks.StackArray(10)
for i in range(10):
	array4.items[i] = i
array4popped = stacks.StackArray(10)
for i in range(9):
	array4popped.items[i] = i
array5 = stacks.StackArray(10)
for i in range(10):
	array5.items[i] = i

#Linked list test stacks

linked3 = stacks.StackLinked(10)
for i in range(5):
	stacks.StackLinked.push(linked3, i)
	#print(linked3.items)
linked4 = stacks.StackLinked(10)
for i in range(6):
	stacks.StackLinked.push(linked4, i)
	#print(linked4.items)
linked5 = stacks.StackLinked(10)
for i in range(10):
	stacks.StackLinked.push(linked5, i)
	#print(linked5.items)
linked6 = stacks.StackLinked(10)
for i in range(9):
	stacks.StackLinked.push(linked6, i)
	#print(linked6.items)
stacks.StackLinked.push(linked6, None)

class Test_Stacks(unittest.TestCase):
	
	def test_is_empty(self):
		self.assertTrue(stacks.StackArray.is_empty(array1))
		self.assertTrue(stacks.StackLinked.is_empty(linked1))

	def test_is_full(self):
		self.assertFalse(stacks.StackArray.is_full(array1))
		self.assertFalse(stacks.StackLinked.is_full(linked1))
		self.assertTrue(stacks.StackArray.is_full(array2))
		self.assertTrue(stacks.StackLinked.is_full(linked2))

	def test_push(self):

		with self.assertRaises(IndexError):
			stacks.StackArray.push(array2, 1)
		with self.assertRaises(IndexError):
			stacks.StackLinked.push(linked2, 1)
		#print("array 3 ", array3.items)
		stacks.StackArray.push(array3, 5)
		#print("array 3 after push", array3.items)
		self.assertEqual(array3.items, array3pushed.items)

		stacks.StackLinked.push(linked3, 5)
		#print(linked3.items)
		for i in range(10):
			self.assertEqual(linked3.items.data, linked4.items.data)

	def test_pop(self):
		with self.assertRaises(IndexError):
			stacks.StackArray.pop(array1)
		with self.assertRaises(IndexError):
			stacks.StackLinked.pop(linked1)

		#print("array 4", array4.items)
		stacks.StackArray.pop(array4)
		#print("array 4 after pop", array4.items)
		self.assertEqual(array4.items, array4popped.items)


		stacks.StackLinked.pop(linked5)
		#print(linked5.items)
		for i in range(10):
			#print(linked5.items.data , ".......", linked6.items.data)
			self.assertEqual(linked5.items.data, linked6.items.data)

	def test_peek(self):
		with self.assertRaises(IndexError):
			stacks.StackArray.pop(array1)
		with self.assertRaises(IndexError):
			stacks.StackLinked.pop(linked1)

		arraypeek = stacks.StackArray.peek(array5)
		#print("this is the top of the stack", arraypeek)

		linkedpeek = stacks.StackLinked.peek(linked2)
		#print("This is the top of the stack", linkedpeek)
		self.assertEqual(linkedpeek, 9)


	def test_size(self):

		arraysize = stacks.StackArray.size(array5)
		#print("The array list size is", arraysize)
		linkedsize = stacks.StackLinked.size(linked2)
		#print("The linked list size is" , linkedsize)


if __name__ == '__main__':
   unittest.main()
