# There are various methods of writing modules
# 1) create a file with a .py extension that contains functions and variables.
# 2) Write module in C language and when compiled, It can be used in python Standard Python Interpreter.

# Execute cmd line args in PyCharm: Run-->Run-->select module-->Edit-->parameter separated by space.-->Apply-->Run
# cmd>
#     python 19_cmd_line_args_module.py Ravi Kiran Goru Guntur

import sys
import os

print(f'sys.argv[0] is always holds the fully qualified file name : \n{sys.argv[0]}')
print(f'Command line arguments are {sys.argv}')


for i in sys.argv:
    print(i)

# sys.path is same as the PYTHONPATH environment variable
print(f'\nPython path: {sys.path}')

print(f'os.getcwd() : {os.getcwd()}')