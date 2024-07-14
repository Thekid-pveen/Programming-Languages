# title: More Variables and Printing
# Love is always a leap into the unknown
"""
STUDY DRILLS:
------------
Strings are really handy, so in this exercise you will learn how to make strings
that have variables embedded in them. You embed variables inside a string by
using a special {} sequence and then put the variable you want inside the {}
characters. You also must start the string with the letter f for “format,” as in
f"Hello {somevar}". This little f before the " (double-quote). 

"""

my_name = 'Pravee'
fav_color = 'white'
girl_frd = 'Rekshi'
my_dog = 'apoo'

print(f"Let's talk about {my_name}.")
print(f'my favourite color is {fav_color}.')
print(f'I like my girl friend {girl_frd}.')
print(f"my dog name is {my_dog}.")

me_and_she = my_name + girl_frd

print(f"me_and_she.")