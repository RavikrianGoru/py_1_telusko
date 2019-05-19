# Base conversion functions bin(), oct(), hex()
print('Different forms of integers')
a = 12
print('a = 12 decimal: ', a)
a = 0b111
print('a = 0B111 or 0B111 Binary: ', a)
a = 0o12
print('a = 0o12 or 0O12 Octal: ', a)
a = 0xbeef
print('a = 0xbeef or 0Xbeef hexa: ', a)

print('bin(decimal/octa/hexa)')
print('bin of 20', bin(20))
print('bin of 0o20', bin(0o20))
print('bin of 0x20', bin(0x20))

print('\noct(decimal/bin/hexa)')
print('oct of 25', oct(25))
print('oct of 0b1101', oct(0b1101))
print('oct of 0xbeef', oct(0xbeef))

print('\nhex(decimal/bin/hexa)')
print('hex of 25', hex(25))
print('hex of 0b1101', hex(0b1101))
print('hex of 0o432', hex(0o432))
