#from array import *
#import array as arr

import array

from builtins import print

values =array.array('i',[10,34,2,-5])
values.reverse()
print(values)
print(values.buffer_info())
print(values.typecode)

values.reverse()
print(values)
print(values[1])

for i in range(len(values)):
    print(values[i])
print("-------")
for i in values:
    print(i)

charS= array.array('u',['a','e','i','0','u'])
print(charS)



newArra= array.array(values.typecode, (a for a in values))
print(newArra)

newArra= array.array(values.typecode, (a*a for a in values))
print(newArra)
sorted(values)
print("Sorted:", values)


a = array.array('i',[])
print(a)
a.append(10)
a.insert(1,20)
a.insert(5,10)
print(a)
print(a.index(20))
print(a.pop())
print(a)
print(a.remove(10))
print(a)


