import functools

def is_even(a):
    return a%2==0


def do_squares(a):
    return a*a


def add_nums(a, b):
    return a+b


nums = [1,2,3,4,5,6,7,8,9,10]

print('\n---------------filter(-,-)-------------')
evens = list(filter(is_even, nums))
print("filter(-,-) with function:", evens)
evens = list(filter(lambda a: a % 2 == 0, nums))
print("filter(-,-) with lambda:", evens)

print('\n---------------map(-,-)-------------')
squares = list(map(do_squares,evens))
print("map(-,-) with function:", squares)
squares = list(map(lambda a: a*a,evens))
print("map(-,-) with lambda:", squares)

print('\n---------------reduce(-,-)-------------')
print('It is available in functools')
total_nums = functools.reduce(add_nums, nums)
print("functools.reduce(-,-) with function:", total_nums)
squares = functools.reduce(lambda a,b: a+b, evens)
print("functools.reduce(-,-,-) with lambda:", total_nums)
