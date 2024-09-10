# title: Prompting and Passing
# More Input you can make
"""
STUDY DRILLS:
-------------
Let’s do one exercise that uses argv and input together to ask the user
something specific. You will need this for the next exercise where you learn to
read and write files. In this exercise we’ll use input slightly differently by
having it print a simple > prompt.
"""
from sys import argv

script, name, passwd = argv
prompt = '# '

print("Your Script is : ",script)

print(f"Hi your name is {name} and you password {passwd}.")

print("\nI ask some questions ?")

print("\nDo you Like my Name : ")
like = input(prompt)

print("\nDo you have a PC or Labtap : ")
pc = input(prompt)

print(f"""
Nice name buddy {name}.
And you have good {pc} system.
your name {name} and {passwd}.
""")
