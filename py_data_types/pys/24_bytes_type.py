#l = [10, 20, 30, 10, 256] #ValueError: bytes must be in range(0, 256)
#l = [10, 20, 30, 10, 'ravi'] #TypeError: 'str' object cannot be interpreted as an integer

l = [10, 20, 30, 10,]
b = bytes(l)
print(type(b), b)

for i in b:
    print(i)

print(b[0])
b[0] = 100 #TypeError: 'bytes' object does not support item assignment
