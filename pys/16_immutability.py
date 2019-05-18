x = 10
y = 10
print('x = {} address is {}'.format(x,id(x)), 'y = {} address is {}'.format(y, id(y)),  'x is y = {}'.format(x is y), sep='\n')

x = x + 1
print('x = {} address is {}'.format(x,id(x)), 'y = {} address is {}'.format(y, id(y)),  'x is y = {}'.format(x is y), sep='\n')


x = 10 + 20j
y = 10 + 20j

print('x = {} address is {}'.format(x,id(x)), 'y = {} address is {}'.format(y, id(y)),  'x is y = {}'.format(x is y), sep='\n')

# any fundamental data types
print("If both objects pointing to same address", x is y)