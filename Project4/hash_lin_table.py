import string
""" Contains the implementation of the HashTable with linear probing and its support functions to create 
a complete concordance of the input file
"""

class LineEntry:
   def __init__(self, word = None, lines = None):
      self.word = word
      #make lines a list containing the lines that the word appears in (for when a word shows up a lot)
      self.lines = lines

class HashTableLinPr:
   def __init__(self, table_size = 251):
      self.table_size = table_size
      self.table = [None]*table_size
      self.num_items = 0
      self.num_collisions = 0

   def insert(self, key, item):
		#helper function to insert words into hashtable (will be called in a loop)
      insertspot = self.myhash(key, self.table_size)
      #get the insert spot
      #insertspot = h_value%self.table_size
      #check the insert spot for that key 

      if(self.get_load_fact() > 0.5):
         #rehash the entire table
         self.grow_table()

      if(self.table[insertspot] == None):
         # insert at spot since it is empty
         lines = []
         lines.append(item)
         self.table[insertspot] = LineEntry(key, lines)
         self.num_items+=1

      else:
         #since it is not empty, check if the word is the same, if so add the line number, if not then linear or quadratic probe
         #it will not append the line number to lines if it is already in lines
         if(self.table[insertspot].word == key and item not in self.table[insertspot].lines): 
            #then add the line number to lines (this counts as a collision)
            self.table[insertspot].lines.append(item)

         elif(item not in self.table[insertspot].lines):
            #go through the linear probing
            # for linear: 
            # while the spot is not empty
            #move over by one each time until you find a empty slot
            #for quadratic:
            # move over by the square of a value which is incremented by one
            spot = insertspot

            #print("The size of the table is: ", len(self.table))
            while(self.table[spot] != None):
               if(spot < self.table_size-1):
                  spot +=1
               else:
                  spot = 0

            #insert at the empty spot found from linear probing
            lines = []
            lines.append(item)
            self.table[spot] = LineEntry(key, lines)
            self.num_items+=1

   def grow_table(self):
      #helper function to insert
      oldtable = self.table
      self.table_size = (self.table_size*2) + 1
      self.table = [None]*self.table_size
      for i in range(len(oldtable)):
         if(oldtable[i] != None):
            word = oldtable[i].word
            lines = oldtable[i].lines
            self.insert(word, lines)

   def myhash(self, key, table_size):
      #computes the hash from a string using horner's rule
      h_value = 0
      n = min(len(key), 8)
      for i in range(n):
         h_value += ((ord(key[i])) * 31)
      return h_value%table_size

   def get_load_fact(self):
		#return the load factor
      load = self.num_items/self.table_size
      return float(load)

   def get_table_size(self):
      return self.table_size

   def read_stop(self, filename):
      #reads words from the stop file and inserts into hash table
      stopfile = open(filename, 'r')
      #list containing each line
      stoplist = stopfile.readlines()
      
      #sort through the lines and insert into the hashtable word by word
      for line in range(len(stoplist)):
         lines  = stoplist[line].split()
         #line is the line number
         for word in range(len(lines)):
            #insert stop words into hash table
            self.insert(lines[word], line)

      stopfile.close()
   def is_num(self, num):
      try:
         float(num)
         return True
      except ValueError:
         return False

   def remove_punct(self, word):
      newword = ''.join(l for l in word if l not in string.punctuation)
      return newword

   def contains(self, word, table):
      #returns true if in stoplist, false if not
      insertspot = self.myhash(word, self.table_size)
      if(table[insertspot] != None and table[insertspot].word == word):
         return True
      else:
         return False


   def read_file(self, filename, stop_table):
      #reads the main file and inserts each word into the hash table, filtering out the stop_table items
      #print(stop_table.table)
      #put the stop words into a list
      stoplist = []
      for i in range(len(stop_table.table)):
         if(stop_table.table[i] != None):
            stoplist.append(stop_table.table[i].word.strip('\n'))
      #print(stoplist)
      #read the main file
      mainfile = open(filename, 'r')
      mainlist = mainfile.readlines()
      mainlist = self.modify(mainlist)
      #print(stoplist)

      for i in range(len(mainlist)):
         self.remove_punct(mainlist[i])
         line = mainlist[i].split()
         for x in range(len(line)):
            #print(line[x] not in stoplist)
            
            if(self.is_num(line[x]) == False and line[x] not in stoplist):
               #print("passed")
               #insert words into hash table since they are not a number and are not in stoplist
               #print(line[x])
               self.insert(self.remove_punct(line[x].strip()), i+1)
               #print("blocked")
   
   def modify(self, lines):
      returnlist = []
      for i in range(len(lines)):
         temp = lines[i]
         temp = temp.lower()
         temp = temp.replace('-',' ')
         temp = temp.replace('\"','')
         temp = temp.replace('\'','')
         temp = temp.replace('?','')
         temp = temp.replace('!','')
         temp = temp.replace(',','')
         temp = temp.replace(':','')
         temp = temp.replace('.','')
         temp = temp.replace(')',' ')
         temp = temp.replace(')',' ')
         returnlist.append(''.join(temp))
      return returnlist

   def list2string(self, lines):
      out = ''
      for i in range(len(lines)):
         if(i == len(lines)):
            out += str(lines[i])
         else:
            out += str(lines[i]) + ' '
      return out

   def save_concordance(self, outputfilename):
      #outputs a file with the format shown in the project description
      outfile = open(outputfilename, 'w')

      #sort through alphabetically
      #sort out the Nones
      sortedtable = []
      wordsonly = []

      for i in range(len(self.table)):
         if(self.table[i] != None):
            wordsonly.append(self.table[i])

      sortedtable = sorted(wordsonly, key=lambda LineEntry: LineEntry.word)
      #for i in range(len(sortedtable)):
      #   print(sortedtable[i].word)

      #iterate through the hash table and write to the output file
      for i in range(len(sortedtable)):
         if(sortedtable[i] != None):
            outstr = sortedtable[i].word +':\t'+ self.list2string(sortedtable[i].lines)
            if(i == 0):
               outfile.write(outstr)
            else:
               outfile.write('\n')
               outfile.write(outstr)

      outfile.close()


      




