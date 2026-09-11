# import mymodule 

# print(mymodule.country)  # Output: USA

# import mymodule as mm

# print(mm.country)  # Output: USA

# mm.say_hi("Mike")  # Output: Hi, Alice!

# from mymodule import say_hi 

# say_hi("Mike2")  # Output: Hi, Mike

import mymodule
print(__name__)
print(mymodule.__name__)

mymodule.cheese.say_cheese()