# More Files
# Working more with Files
"""
STUDY DRILLS:
-------------
Now let’s do a few more things with files. We’ll write a Python script to copy
one file to another. It’ll be very short but will give you ideas about other things
you can do with files. You should immediately notice that we import another handy 
command named exists. This returns True if a file exists, based on its name in a 
string as an argument. It returns False if not.
"""
from sys import argv
from os.path import exists # find the file is exists or not

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file) #variable to open() file
in_data = in_file.read()  # variable to read() the file

print(f"the input file is {len(in_data)} bytes long") # len() to find storeage value

print(f"Does the output file exist? {exists(to_file)}") # retrun true read above "..."
print("Ready, hit RETURN to continue, CTRL-C to abort.") 
input("?")

out_file = open(to_file, 'w') # another variable to open() and write:'w', the to_file
out_file.write(in_data) # write() the file into from file

print("Alright, all done")

out_file.close() 
in_file.close()
