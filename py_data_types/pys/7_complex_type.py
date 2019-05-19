# Complex data type
x = 10+20j
print('x = 10+20j', x, type(x), x.real, x.imag)
x = 10+20J
print('x = 10+20J', x, type(x), x.real, x.imag)

print('\nComplex number has two parts (real and imaginary parts)')
print('real parts can be integer(decimal/bin/oct/hex form) or float(decimal form)')
a = 0b1011 + 20j
print('a = 0b1011 + 20j', a, type(a), a.real, a.imag)
b = 0o12 + 20j
print('b = 0o12 + 20j', b, type(b), b.real, b.imag)
c = 0x12 + 20j
print('c = 0x12 + 20j', c, type(c), c.real, c.imag)
d = 10.5 + 20.7j
print('d = 10.5 + 20.7j', d, type(d), d.real, d.imag)

print('We can perform arthmetic operations: ')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
#print(a // b) Can not perform this operations
