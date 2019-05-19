name = 'ravi'
seat = 28

# string concatenation required string convertion for int here
wish_msg = 'Hello, ' + name + 'your seat number is ' + str(seat)

wish_msg = 'Hello, {0} your seat number is {1}'.format(name, seat)
wish_msg = 'Hello, {} your seat number is {}'.format(name, seat)


wish_msg = 'Hello, {name} your seat number is {seat}'.format(name=name, seat=seat)

# f' formatter string
wish_msg = f'Hello, {name} your seat number is {seat}'
print(wish_msg)


print('{}'.format(24/9))
print('{0:.3f}'.format(24/9))
print('{0:_^10}'.format(name))

# r' raw string
print(r'this is "ravi\navya"')

# backslach \ for combine multiple lines
s = 'this is log line \
we can write mutliple line by backslash'
print(s)


