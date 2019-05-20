import module_using_name as m

# Remember that the module should be placed either in the same directory as the program
# from which we import it, or in one of the directories listed in sys.path

# This will import all public names such as say_hi but would not import __version__
# because it starts with double underscores.

print('hi')
m.say_hi() # no suggestions available for as of now.
m.say_bye()
print(m.__version__)


