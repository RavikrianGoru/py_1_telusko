
# Data types
#int z = 20 SyntaxError
a = 10
b = 10.5
c = True
d = 10+20j
print(a, id(a), type(a))
print(b, id(b), type(b))
print(c, id(c), type(c))
print(d, id(d), type(d))

a = 12
print(a)
a = 0b111
print(a)
a = 0B111
print(a)
a = 0o12
print(a)
a = 0O13
print(a)
a = 0xbeef
print(a)
a = 0Xbeef
print(a)

# Base conversion functions bin(), oct(), hex()

print('bin(-)')
print(bin(20))
print(bin(0o20))
print(bin(0x20))

print('oct(-)')
print(oct(25))
print(oct(0b1101))
print(oct(0xbeef))

print('hex(-)')
print(hex(25))
print(hex(0b1101))
print(hex(0o432))


f = 123.45
print(f, type(f))
f = 12345e-3
print(f, type(f))
f = 12345e3
print(f, type(f))

# complex data type
x = 10+20j
print(x, type(x), x.real, x.imag)
x = 10+20J
print(x, type(x), x.real, x.imag)

a = 0b1011 + 20j
print(a, type(a), a.real, a.imag)
b = 0o12 + 20j
print(b, type(b), b.real, b.imag)
c = 0x12 + 20j
print(c, type(c), c.real, c.imag)
d = 10.5 + 20.7j
print(d, type(d), d.real, d.imag)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
