import array

a = array.array('i',[1,2,3,4,5])
b = array.array('i',[1,2,3,4,5,6])

print("1st array :", a)
print("2nd array :", b)


if len(a) == len(b):
    c = array.array(a.typecode, [])
    for i in range(0, len(a)):
        c.append(a[i]+b[i])
        a[i]+b[i]
    print("Added array:", c)
else:
    print("Both arrays must be in same size")


x = b[0]
for i in b:
    if x < i:
        x = i
print('Max item is :', x)