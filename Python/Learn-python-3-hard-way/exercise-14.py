# title: Prompting and Passing
# More Input you can make

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
