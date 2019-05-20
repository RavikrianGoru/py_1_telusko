# Python treats everything as an object and this includes functions.
# Functions are reusable pices of programs.
# They allow to give a name to a block of statements & allows to run that block by name.
# The pass statement is used in Python to indicate an empty block of statements.

def say_hello():
    # block belong to function
    print('Hello all')
# end of function

def print_max(a,b):
    if a == b:
        print(f'{a} == {b}')
    elif a < b:
        print(f'{a} < {b}')
    else:
        print(f'{a} > {b}')


def empty_function():
    pass


say_hello()
say_hello()
print_max(5,6)
print_max(15,6)
print_max(5,5)
empty_function()
