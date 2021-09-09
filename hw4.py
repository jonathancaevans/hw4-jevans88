#It makes sense to make starting_value an instance variable of the class because
#you can self refrence an object that holds the lengthy operation class and then any
#further changes you'd want to make could just be done by constructing a new class.

import math

class lengthyMathematicalOperation:
	def __init__(self, starting_value, min_value, max_value, coefficient):
		self.starting_value = starting_value
		self.min_value = min_value
		self.max_value = max_value
		self.coefficient = coefficient
		self.res = self.starting_value
		
	def complicated_math_operation(self):
		self.multiply_it()
		self.add_it()
		self.sqrt_it()
		self.compound_op_it()
		
		return self.res

	def multiply_it(self):
		res = max(self.min_value, min(self.max_value, self.starting_value * self.coefficient))

	def add_it(self):
		res = max(self.min_value, min(self.max_value, self.starting_value + self.coefficient))

	def sqrt_it(self):
		res = max(self.min_value, min(self.max_value, math.pow(self.starting_value, -self.coefficient)))

	def compound_op_it(self):
		self.multiply_it()
		self.starting_value = self.res
		self.add_it()
