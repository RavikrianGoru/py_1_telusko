s1 = {10, 20, 'ravi', 35.7}
print('Set s1', s1)
fs1 = frozenset(s1)
print(type(fs1), 'Frozen Set fs1', fs1)
# fs1.add(10) #AttributeError: 'frozenset' object has no attribute 'add'
