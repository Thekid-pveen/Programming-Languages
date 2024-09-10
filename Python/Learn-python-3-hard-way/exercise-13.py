# title: Parameters, Unpacking, Variables
# Hold Up! Features Have Another Name
"""
STUDY DRILLS:
-------------
The argv is the argument variable, a very standard name in programming that
you will find used in many other languages. On line 3 unpacks argv. “unpack” is probably 
the best word to describe what it does. It says, “Take whatever is in argv, unpack it, 
and assign it to all of these variables on the left in order.” 
a script (script being another name for your .py files).

I call them “features” here (these little things you import to make your Python
program do more) but nobody else calls them features. Before
you can continue, you need to learn their real name: modules.

From now on we will be calling these “features” that we import modules. I’ll
say things like, “You want to import the sys module.” They are also called
“libraries” by other programmers, but let’s just stick with modules.
"""
from sys import argv # run the file with argv

script, first, second = argv

print("The Script called is",script)
print("first name is ",first)
print("second name is ",second)
  
