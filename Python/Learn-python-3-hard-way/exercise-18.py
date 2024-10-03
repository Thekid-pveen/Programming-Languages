# title: Names, Variables, Code, Functions
# Fuctions with Arguments
"""
STUDY DRILLS:
-------------
You can create a function by using the word def in Python. I’m going to have
make four different functions, the functions are important to know. 
I will give you the simplest explanation you can use right now.
NOTE: Look out for the *args, which is different * to assign the number of values you can pass.
"""
def function_one(*args):    # *args is pointless
    arg1, arg2 = args      
    print(f"arg1 is {arg1} and arg2 is {arg2}.")

def function_two(arg1, arg2): 
    print(f"arg1 is {arg1} and arg2 is {arg2}.")

def function_three(arg1):
    print(f"arg is {arg1}.")

def function():
    print("Hello, What's up!")

function_one("thekid", "pveen")
function_two("praveen", "pravee")
function_three("hey kid")
function()
