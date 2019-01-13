#lab 8
"""Contains the hash table class and all of its implemented functions. In my implementation, I use the SlotEntry
class to store both the key and item and there is a list of these items per slot
"""

class SlotEntry:
	def __init__(self, key = None, item = None):
		self.key = key
		self.item = item

class MyHashTable:
	def __init__(self, table_size = 11):
		self.table_size = table_size
		self.table = [[] for _ in range(table_size)]
		#create a blank class for each list
		for slot in self.table:
			startingslot = SlotEntry()
			slot.append(startingslot)

		self.num_items = 0
		self.num_collisions = 0

	def insert(self, key, item):
		#get the insert spot
		insertspot = key%self.table_size
		#check the insert spot for that key 
		if(self.table[insertspot][0].key == None):
			# insert at spot since it is empty
			self.table[insertspot][0].key = key
			self.table[insertspot][0].item = item
			#newentry = SlotEntry(key, item)
			#self.table[insertspot].append(newentry)
			self.num_items+=1
		else:
			#there are other keys present, increase collisions
			#first check if they key is already in the list
			check = False
			for i in range(len(self.table[insertspot])):
				if(self.table[insertspot][i].key == key):
					#if it is the same, replacing the item with the new item
					self.table[insertspot][i].item = item
					check = True

			if(check is False):
				#then the key is not in that slot in the hash table, so adding it
				self.num_collisions +=1
				newentry = SlotEntry(key, item)
				self.table[insertspot].append(newentry)
				self.num_items +=1

		if(self.load_factor() > 1.5):
			#rehash the entire table
			self.grow_table()
	
	def grow_table(self):
		oldtable = self.table
		self.table_size = self.table_size*2+1
		self.table = [[] for _ in range(table_size)]
		for i in range(len(oldtable)):
			for x in i:
				key = x.key
				item = x.item
				self.insert(key, item)


	def get(self, key):
		try:
			spot = key%self.table_size
			for i in range(len(self.table[spot])):
				if(self.table[spot][i].key == key):
					return (self.table[spot][i].key, self.table[spot][i].item)
			
		except:
			raise LookupError("Key is not found")

	def remove(self, key):
		try: 
			for i in range(len(self.table)):
				for x in range(len(self.table[i])):
					if(self.table[i][x].key == key):
						itemremoved = self.table[i][x]
						self.table[i][x] = None
			return (itemremoved.key, itemremoved.item)

		except:
			raise LookupError("Key is not found")

	def size(self):
		return self.num_items

	def load_factor(self):
		load = self.num_items/self.table_size
		return float(load)

	def collisions(self):
		#increase when you hash to an occupied spot
		return self.num_collisions
