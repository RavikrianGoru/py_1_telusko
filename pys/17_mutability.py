# list is mutable
l1 = [10, 20, 30, 40]
print(l1, 'address: {}'.format(id(l1)))
l1[0] = 1000
print(l1, 'address: {}'.format(id(l1)))

l2 = l1
l2[3] = 4000
print(l1, 'address: {}'.format(id(l1)))
print(l2, 'address: {}'.format(id(l2)))

