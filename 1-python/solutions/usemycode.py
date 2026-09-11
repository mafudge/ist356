import mycode

print(mycode.person)

mycode.say_hi("Alice")

from mycode import say_hi

say_hi("Bob")

import mycode as local_mycode
print (local_mycode.person)

local_mycode.morecode.say_hi("Charlie")