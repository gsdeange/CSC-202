import unittest
import perm_lex

""" This file will test the perm_gen_lex function in perm_lex and gives
	several test cases to check if the function works properly.
"""

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
    	#test an empty string
        self.assertEqual(perm_lex.perm_gen_lex(''), [''])

        # test one single character
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])

    	#test ab string
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

        #test abc string
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])        


if __name__ == "__main__":
        unittest.main()
