t1 = (10, 20.5, 'ravi', 10, 25)
print(type(t1), t1)
print(t1[0], t1[-5])
print(t1[4],t1[-1])
print(t1[1:4])

# t1[0] = 100 TypeError: 'tuple' object does not support item assignment

t2 = ()
print(type(t2), t2)
t2 = (10) # here t2 is not tuple
print(type(t2), t2) # It's type is int type

t3 = (10,) # here t2 is  tuple
print(type(t3), t3)