# Python has a nifty feature called documentation strings, usually referred to by its shorter name docstrings.
# DocStrings are an important tool that you should make use of since it helps to document
# the program better and makes it easier to understand.

# DocStrings also apply to functions, modules and classes
# DocStings start with Capital letter and ends with .
# 2nd line shuld be blank and from 3rd line give full explanation
# Strongly advised to follow this convention for all our docstrings for all non-trivial functions.
# The pydoc command that comes with your Python distribution works similarly to help() using docstrings.

# Python treats everything as an object and this includes functions.
def print_max(a,b):
    '''Prints maximum of two numbers

 given inputs should be integers.
    '''

    a = int(a)
    b = int(b)
    if a > b:
        print(f'max {a}')
    elif b > a:
        print(f'max {b}')
    else:
        print(f'both are equal')

print_max(10,20)
print(print_max.__doc__)

help(print_max)