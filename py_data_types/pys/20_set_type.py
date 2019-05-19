s1 = {10, 20, 'ravi', 25.6}
s2 = {10, 20, 'ravi', 25.6, 20, 10}
print(type(s1), s1)

# print(s1[0]) TypeError: 'set' object does not support indexing
# print(s1[0:4]) TypeError: 'set' object is not subscriptable

print(s2)
s2.add(50)
print(s2)
s2.remove(10)
print(s2)

s3 = {}
print(type(s3)) # Empty dictionary
s4 = set()
print(type(s4))

