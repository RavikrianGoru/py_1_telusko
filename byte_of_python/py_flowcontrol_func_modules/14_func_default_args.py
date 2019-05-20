# default args: we can assign default values to args in function declaration itself.
# Only those parameters which are at the end of the parameter list can be given default argument values
# Example, def func(a, b=5) is valid, but def func(a=5, b) is not valid.
# here, arguments are position based


def fun_default_arg(name, times=1):
    print(f'Hello {name}' * times)


fun_default_arg('Ravi')
fun_default_arg('Kiran', 3)

