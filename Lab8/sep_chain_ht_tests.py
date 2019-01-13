#sep_chain_ht_tests.py
"""
Contains the tests for all of the hash table functions and tests the boundry cases 
"""

import unittest
from sep_chain_ht import *

class Test_Hash_Table(unittest.TestCase):
	
	def test_insert(self):
		"""hash1 = MyHashTable()
		hash1.insert(11, "hello")
		hash1.insert(1, "pizza")
		hash1.insert(23, "banana")
		hash1.insert(34, "soccer")
		hash1.insert(45, "waffles")
		hash1.insert(56, "banana")
		hash1.insert(67, "soccer")
		hash1.insert(78, "waffles")
		hash1.insert(89, "banana")
		hash1.insert(100, "soccer")
		hash1.insert(111, "waffles")
		hash1.insert(1, "sauce")

		for slot in range(len(hash1.table)):
			print("slot: ", slot)
			for entry in hash1.table[slot]:
				print("key: ", entry.key, " item: ", entry.item)
		print()
		print("table size: ", hash1.table_size)
		print("number of items: ", hash1.num_items)
		print("load factor : ", hash1.load_factor())"""

		hash2 = MyHashTable()
		hash2.insert(0, "pizza")

		self.assertEqual(hash2.table[0][0].key, 0)
		self.assertEqual(hash2.table[0][0].item, "pizza")
		hash2.insert(0, "soccer")
		self.assertEqual(hash2.table[0][0].key, 0)
		self.assertEqual(hash2.table[0][0].item, "soccer")

	def test_get(self):
		hash1 = MyHashTable()
		hash1.insert(0, "pizza")
		self.assertEqual(hash1.get(0), (0, "pizza"))
		hash1.remove(0)
		with self.assertRaises(LookupError):
			hash1.get(0)

	def test_remove(self):
		hash1 = MyHashTable()
		hash1.insert(0, "pizza")
		self.assertEqual(hash1.remove(0), (0, "pizza"))
		with self.assertRaises(LookupError):
			hash1.remove(0)

	def test_load_factor(self):
		hash1 = MyHashTable()
		hash1.insert(0, "pizza")
		load = float(hash1.num_items/hash1.table_size)
		self.assertEqual(hash1.load_factor(), load)

	def test_size(self):
		hash1 = MyHashTable()
		hash1.insert(0, "pizza")
		self.assertEqual(hash1.size(), 1)

	def test_collisions(self):
		hash1 = MyHashTable()
		hash1.insert(0, "pizza")
		self.assertEqual(hash1.collisions(), 0)
	
if __name__ == '__main__':
   unittest.main()