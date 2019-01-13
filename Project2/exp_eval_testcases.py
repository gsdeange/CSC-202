import unittest
import exp_eval
""" Contains the test cases for all of the exp_eval functions and helper functions. The postfix_eval function will
raise a Value Error if the expression tries to divide by zero.
"""
#exp_eval.infix_to_postfix("1 + 2 + 3")
#print(exp_eval.isnum("7"))



class Test_Exp_Eval(unittest.TestCase):

	def test_is_num(self):
		self.assertTrue(exp_eval.is_num("7"))
		self.assertTrue(exp_eval.is_num("-7"))
		self.assertFalse(exp_eval.is_num("+"))

	def test_infix_to_postfix(self):
		#print(exp_eval.infix_to_postfix("1 + 2 + 3"))
		#print(exp_eval.infix_to_postfix("1 + 2 * 3 + 4"))
		#print(exp_eval.infix_to_postfix("2 ^ 3"))
		self.assertEqual(exp_eval.infix_to_postfix("1 + 2 * 3"), ("1 2 3 * +"))
		self.assertEqual(exp_eval.infix_to_postfix("1 + 2 ^ 3 + 4"), ("1 2 3 ^ + 4 +"))

	def test_postfix_valid(self):
		#print(exp_eval.postfix_valid(exp_eval.infix_to_postfix("1 + 2 + 3")))
		
		self.assertFalse(exp_eval.postfix_valid("1 + 2 + 3"))
		self.assertTrue(exp_eval.postfix_valid("1 2 3 * + 4 +"))

	def test_postfix_eval(self):
		#print("evaluation")
		self.assertEqual(exp_eval.postfix_eval(exp_eval.infix_to_postfix('1 + 2 + 3')), 6)
		self.assertEqual(exp_eval.postfix_eval(exp_eval.infix_to_postfix("1 + 2 * 3 + 4")), 11)
		self.assertEqual(exp_eval.postfix_eval(exp_eval.infix_to_postfix("1 + 2 ^ 3 / 3")), 3)

		with self.assertRaises(ValueError):
			exp_eval.postfix_eval(exp_eval.infix_to_postfix("1 + 2 * 3 / 0"))
		



if __name__ == '__main__':
   unittest.main()
