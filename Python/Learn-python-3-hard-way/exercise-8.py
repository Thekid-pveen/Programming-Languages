# title: Printing, Printing
# Printing is a good visualization
"""
STUDY DRILLS:
-------------
In this exercise I’m using something called a function to turn 
the formatter variable into other strings. When you see me 
write formatter.format(...) I’m telling python to do the following
"""

formatter_str = " {} {} {} "

lycris_1 = formatter_str.format("Okay,", "I realize now,", "that everything that I did was wrong")
lycris_2 = formatter_str.format("Okay,", "I realize now,", "some things are better off said than done")
lycris_3 = formatter_str.format("Okay,", "I realize now,", "that maybe I'm not ready for love")
lycris_4 = formatter_str.format("Okay,", "I realize now,", "I finished us before we begun-un-un")

numbers = formatter_str.format(1, 2, 3)

boolens = formatter_str.format(True, False, True)

emty = formatter_str.format(formatter_str, formatter_str, formatter_str)

print(lycris_1)
print(lycris_2)
print(lycris_3)
print(lycris_4)

print(numbers)
print(boolens)
print(emty)