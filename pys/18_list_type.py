# list duplicate and insertion order.
l1 = [10, 20.5, 'ravi', 10, 25]
print(type(l1), l1)

l2 = []
l2.append(10)
l2.append(20)
l2.append(30)
l2.append(30)
l2.append(40)
print(l2)
l2.remove(30)
print(l2)
l2[0] = 100

print(l2)