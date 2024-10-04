# title: Functions and Files
# I'm not learned at this point

"""
Study Drills:
Write a comment for each line to understand what that line does. make sure I clarify that
argv, and three functions, the first function is to read the file, the second function goes 
on the poniter position and the third function is printing line just using number.
"""

from sys import argv

script, input_file = argv

def print_all(f):
        print(f.read())

def rewind(f):
        f.seek(0)

def print_a_line(line_count, f):
        print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)
