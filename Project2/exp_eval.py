#exp_eval.py
import Stacks
import math
""" contains three main functions: infix_to_postfix, postfix_valid, and postfix_eval. The first converts infix to postfix,
the second takes in a string and checks if it is a valid postfix expression. The last one will take in the postfix expression
and evaluate the expression to produce a result
"""

def is_num(num):
	#checks if the string is a number
	if(num[0] in ('-', '+')):
		return num[1:].isdigit()
	return num.isdigit()
def precedence(operator):
	#returns value of precedence
	if(operator == '+' or operator == "-"):
		return 1
	elif(operator == '*' or operator == '/'):
		return 2
	elif(operator == "^"):
		return 3
	else:
		return 4

def  infix_to_postfix(infix_expr):
	
	#take in string with infix expression
	#use .split function to break up the string into a list
	#create a stack that will hold the operators, and a outputlist that contains the numbers and the entire postfix expression
	#in a loop, add numbers to the outputlist and push operators onto the stack. 
	#if the operator is of equal or higher precedence(higher in order of operations), then pop it off the stack
	#add then to the outputlist with the numbers.

	returnlist = []
	expression = infix_expr.split(' ')
	#print(expression)

	operatorstack = Stacks.StackArray(30)

	#putting characters in the the list
	for character in expression:
		if(is_num(character)):
			returnlist.append(character)
		else:
			#check if the top of the stack is a higher precedence than the current character
			while (not operatorstack.is_empty()) and (precedence(operatorstack.peek()) >= precedence(character)):
				#add the top of the stack to the output list
				operatorstack.pop()
				returnlist.append(operatorstack.items[operatorstack.size()])
			operatorstack.push(character)

	while(not operatorstack.is_empty()):
		operatorstack.pop()
		returnlist.append(operatorstack.items[operatorstack.size()])

	return ' '.join(returnlist)	

def postfix_valid(string):
	if(string == ''):
		return False
	else:
		characterlist = string.split(' ')
		count = 0
		for i in range(len(characterlist)):
			if(is_num(characterlist[i])):
				count +=1
			else: 
				count-=2
				if(check_count(count) != True):
					return False
				count+=1
		if(count != 1):
			return False
	return True

def check_count(count):
	if(count >= 0):
		return True
	return False

def postfix_eval(postfix_expr):
	
	operatorstack = Stacks.StackArray(30)
	characterlist = postfix_expr.split(' ')

	for character in characterlist:
		if(is_num(character)):
			operatorstack.push(int(character))
		else:
			operatorstack.pop()
			op2 = operatorstack.items[operatorstack.size()]
			operatorstack.pop()
			op1 = operatorstack.items[operatorstack.size()]
			result = operate(character, op1, op2)
			operatorstack.push(result)
	operatorstack.pop()
	return int(operatorstack.items[operatorstack.size()])



def operate(operand, op1, op2):
	if(operand == '*'):
		return op1*op2
	elif(operand == "/"):
		if(op2 == 0):
			raise ValueError
		return op1/op2
	elif(operand == '+'):
		return op1 + op2
	elif(operand == "^"):
		return math.pow(op1, op2)
	else:
		return op1 - op2

