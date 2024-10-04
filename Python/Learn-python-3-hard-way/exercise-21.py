# Functions Can Return Something
# Function 
"""
STUDY DRILLS:
-------------
We are now doing our math functions for adding, subtracting, multiplying, and dividing.
Return to calculate the value just enough. This exercise might whack your brain out,
but treat it slowly and easily like a little game.
"""
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b
	
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b
	
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b
	
print("Let's do some math with just functions!")

age = add(19, 2)
height = subtract(69, 1)
weight = multiply(10, 6)
iq = divide(200, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print("That is a collapse in " + what)
