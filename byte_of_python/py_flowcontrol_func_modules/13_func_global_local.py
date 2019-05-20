x = 50
y = 100
z = 150

def x_local(x):
    x = 51 # x is local variable
    y = 101 # x is local variable
    z = 151 # x is local variable

    print(f'x {x} y {y} z {z} inside function')


def x_global():
    global x, y, z # x , y, z are global variables
    x = 51
    y = 101
    z = 151
    print(f'x {x} y {y} z {z} inside function')


print(f'x {x} y {y} z {z} initial values global')
x_local(x)
print(f'x {x} y {y} z {z} updated values global')

print('------')
print(f'x {x} y {y} z {z} initial values global')
x_global()
print(f'x {x} y {y} z {z} updated values global')