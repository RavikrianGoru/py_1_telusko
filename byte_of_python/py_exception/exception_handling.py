
# try....except....else
# finally

try:
    text = input('Enter your input:')
except (EOFError, KeyboardInterrupt):
    print('End of file entered.')
except KeyboardInterrupt:
    print('KeyboardInterrupt occurred.')
else:
    print('You entered {}'.format(text))
