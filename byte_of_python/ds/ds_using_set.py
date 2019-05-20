# Sets are unordered collections of simple objects. These are used when the existence of an
# object in a collection is more important than the order or how many times it occurs.
cities = {'gnt','mas','vij'}
print('all cities set:', cities)
names = ['gnt', 'mas', 'vij', 'gnt']
print('all names list:', names)
s = set(names)
print('all names set:', s)

print(f'ravi in s : {"gnt" in s}')
print(f'ravi not in s : {"gnt" not in s}')
s.add('hyd')
print(s)
print(f's.issubset(cities) = {s.issubset(cities)}')
print(f's.issuperset(cities) = {s.issuperset(cities)}')
print(f's.issuperset(names) = {s.issuperset(names)}')

print(f'cities | s = {cities | s}')
print(f'cities.union(s) = {cities.union(s)}')

print(f'cities & s = {cities & s}')
print(f'cities.intersection(s) = {cities.intersection(s)}')

# print(f'cities & names = {cities & names}') # TypeError: unsupported operand type(s) for &: 'set' and 'list'
