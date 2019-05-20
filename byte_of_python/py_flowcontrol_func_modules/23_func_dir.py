# The built-in dir() function returns the list of names defined by an object.
# If the object is a module, this list includes functions, classes and variables, defined inside that module.

# This function can accept arguments. If the argument is the name of a module, the function
# returns the list of names from that specified module. If there is no argument, the function
# returns the list of names from the current module.

import sys
import module_using_name as m

print(dir(sys))
for each in dir(m): # m as module_using_name
    print(each)

for each in dir(): # current module
    print(each)

print('-----------------')
a = 10
print(dir())
del a
print(dir())

