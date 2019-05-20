# The return statement is used to return from a function i.e. break out of the function.
# return statement is optional

def max_ab(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 'equal'
def say_hi():
    print('Hi')


print(f'max of 10, 20 :{max_ab(10,20)}')
print(f'max of 21, 11 :{max_ab(21,11)}')
print(f'max of 20, 20 :{max_ab(20,20)}')

print('None will be return by default:')
print(say_hi())

# TypeError: can only concatenate str (not "NoneType") to str
