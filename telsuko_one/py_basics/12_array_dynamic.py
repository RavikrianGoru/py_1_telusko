from array import *

values = array('i',[])
print("Empty array:",values)

x = int(input("Enter length of array:"))

i =0
while i<x:
    e =int(input("Enter next element:"))
    values.append(e)
    i+=1
print(values)

# print(values.index(s)) # build in function
s = int(input("Enter element to search:"))
itr = 0
for each in values:
    if s == each:
        print(itr)
        break
    itr+=1
else:
    print("element Not Found")



