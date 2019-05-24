
l = [2,4,6,1,3]
print('iterate a list by index')
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

print('iterate a list by while')
i =0;
while i<len(l):
    print(l[i])
    i+=1

print('iterate a list by for loop-1')
for i in range(0,len(l)):
    print(i)

print('iterate a list by iterator')
for i in iter(l):
    print(i)

print('--------------------------')

itr = iter(l)
print("itr = ", itr)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(next(itr))
print(next(itr))
print('The next statement throws StopIterator')
print(next(itr))
print(next(itr))



