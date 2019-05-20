# Python program is also a module.

# __name__ is used for the particular purpose of figuring out whether the module is being
# run standalone or being imported.

# when a module is imported for the first time, the code it contains gets executed.

__version__ = '0.1'


def say_hi():
    print('Hi, I am module_using_name module speaking')

def say_bye():
    print('Bye, I am module_using_name module speaking')


if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
