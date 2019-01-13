#huffman.py
"""contains the huffmannode class and all of the functions dedicated to implementing the huffman codes, decoding and encoding
"""
class HuffmanNode:
   def __init__(self, char, freq):
      self.char = char  # actually the character code
      self.freq = freq
      self.left = None
      self.right = None

   def set_left (self, node):
      self.left = node

   def set_right (self, node):
      self.right = node

def comes_before (a, b) :
   """returns true if tree rooted at node a comes before tree rooted at node b """
   if(a.freq < b.freq):
      return True
   elif(a.freq == b.freq):
      if(a.char < b.char):
         return True
   return False


def combine (a, b) :
   """ creates a new huffman node with children a and b with combined freq and lower value char """
   newfreq = a.freq+b.freq
   if(a.char < b.char):
      newchar = a.char
   else:
      newchar = b.char
   newnode = HuffmanNode(newchar, newfreq)
   newnode.set_left(a)
   newnode.set_right(b)
   return newnode

def create_list(size):
   return [0]*size
def create_string_list(size):
   return ['']*size

def cnt_freq(filename):
   try:
      text = open(filename, 'r')
   except:
      raise IndexError("file not found")
   characters = text.readline()
   countlist = create_list(256)
   for i in range(len(characters)):
      countlist[ord(characters[i])] +=1
      #print(characters[i], "   : ", ord(characters[i]))
      
   text.close()
   return countlist

def insert_sorted(alist, node):
   if(len(alist) == 0):
      alist.append(node)
   else:
      flag = False
      for i in range(len(alist)):
         if(comes_before(node, alist[i]) and not flag):
            alist.insert(i, node)
            flag = True
      if(flag == False):
         alist.append(node)      

def create_huff_tree(freqs):
   treelist = []
   for i in range(len(freqs)):
      if(freqs[i] > 0):
         newnode = HuffmanNode(ord(chr(i)), freqs[i])
         insert_sorted(treelist, newnode)

   while len(treelist) > 1:
      combined = combine(treelist[0], treelist[1])
      treelist = treelist[2:]
      insert_sorted(treelist, combined)

   return treelist[0]

def create_map(node, codelist, prefix):
   #print(prefix)
   if(node.left != None):
      #prefix += '0'
      create_map(node.left, codelist, ''.join((prefix, '0')))
   if(node.right != None):
      #prefix += '1'
      create_map(node.right, codelist, ''.join((prefix, '1')))
   if(node.left == None and node.right == None):
      codelist[node.char] = prefix
   
   
def create_code(root_node):
   codelist = create_string_list(256)
   current = root_node
   create_map(current, codelist, '')
   
   return codelist

def tree_preord(root_node):
   returnstring = ''
   preord = []
   tree_preord_helper(root_node, preord)
   return ''.join(preord)

   return returnstring
def tree_preord_helper(root, preord):
   if(root.left == None and root.right == None):
      preord.append('1')
      preord.append(chr(root.char))
   else:
      preord.append('0')
      tree_preord_helper(root.left, preord)
      tree_preord_helper(root.right, preord)


def huffman_encode(in_file, out_file):
   try:
      inputfile = open(in_file, 'r')
   except:
      raise IndexError("file not found")
   preord = inputfile.readline()
   inputfile.close()
   freqlist = cnt_freq(in_file)
   hufftree = create_huff_tree(freqlist)
   codes = create_code(hufftree)
   
   outputlist = []
   for i in range(len(preord)):
      outputlist.append(codes[ord(preord[i])])

   outputfile = open(out_file, 'w')
   outputfile.write(''.join(outputlist))
   outputfile.close()


def huffman_decode(freqs, encoded_file, decode_file):
   try:
      encoded = open(encoded_file, 'r')
   except:
      raise IndexError("file not found")
   encodedlist = encoded.readline()
   encoded.close()
   hufftree = create_huff_tree(freqs)

   decodedlist = []
   current = hufftree
   for i in range(len(encodedlist)):
      if(encodedlist[i] == '0'):
         current = current.left
      elif(encodedlist[i] == '1'):
         current = current.right
      if(current.left == None and current.right == None):
         decodedlist.append(chr(current.char))
         current = hufftree
   output = open(decode_file, 'w')
   output.write(''.join(decodedlist))
   output.close()
      






