l = [10, 20, 10, 23, 14]
b = bytearray(l)
print(type(b), b)
for i in b:
    print(i, end=" ")

print(b[0])
b[0] = 100 # bytearrya is mutable

for i in b:
    print(i, end=" ")
