# title: Reading Files  
# Working with files
"""
STUDY DRILLS:
-------------
This exercise involves writing two files. One is the usual ex15.py file that you
will run, but the other is named sample.txt this one you want to created. This second file isn’t a
script but a plain text file we’ll be reading in our script. the new commands are open() & read() stay focus.
"""
from sys import argv

script, filename = argv

txt = open(filename) 

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type filename again : ")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read()) 
