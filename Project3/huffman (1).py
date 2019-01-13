
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

def combine (a, b) :
	""" creates a new huffman node with children a and b with combined freq and lower value char """

def cnt_freq(filename):

def create_huff_tree(char_freq):

def create_code (node):

def tree_preord (node):

def huffman_encode(in_file, out_file):

def huffman_decode(freqs, encoded_file, decode_file):
