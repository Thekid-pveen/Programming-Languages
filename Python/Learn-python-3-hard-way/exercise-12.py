# title: Prompting People
# Put Into Variable In Input
"""
STUDY DRILLS:
-------------
This is how you ask someone a question and get the answer, Put a string that you want
for the prompt inside the () so that it looks like this: x = input("Name? "), 
these the exercise is also like the previous one using just input to do all the prompting.

"""
py = input("What Programming Language Do you Learn ?")
ecs = input("Eat Code SLeep ?")
ai = input("AI stands for ?")

print("\ndifference between Last ex and this program ?\n",end=' ')
diff=input("input() takes no keyword arguments")

print(diff)

print(f"""ok. Now you learn {py} and your mindset is {ecs}.
you know AI: {ai}.""") 
