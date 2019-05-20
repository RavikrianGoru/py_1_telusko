# Keyword args: we can pass function args by name.
# keyword arguments - we use the name (keyword) instead of the position

# There are two advantages -
# one, using the function is easier since we do not need to worry about the order of the arguments.
# Two, we can give values to only those parameters to which we want to, provided that the other parameters have default argument values.


def fun_keyword_args(a, b=10, c=20):
    print(f'a {a} b {b} c {c}')
    # a is position param
    # b,c are keyword params


fun_keyword_args(1)
fun_keyword_args(1,c=21)
fun_keyword_args(10,b=31)

#TypeError: fun_keyword_args() missing 1 required positional argument: 'a'
#fun_keyword_args(b=25,c=35)

