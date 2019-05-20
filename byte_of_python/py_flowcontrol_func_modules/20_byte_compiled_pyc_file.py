# Importing a module is a relatively costly affair.
# Python does some tricks to make it faster
# One way is to create byte-compiled files with the extension .pyc
# which is an intermediate form that Python transforms the program into

# This .pyc file is useful when you import the module the next time from a
# different program - it will be much faster since a portion of the processing required in
# importing a module is already done.

# NOTE: These .pyc files are usually created in the same directory as the corresponding
# .py files. If Python does not have permission to write to files in that directory, then the
# .pyc files will not be created.


# Avoid using
#   'from sys import argv' as it causes name clashes
from os import getcwd
from math import sqrt

print(f'getcwd() : {getcwd()}')
print("Square root of 16 is", sqrt(16))
