import numpy

# array doen not support multi dimension arrays.
#ary = array.array('i',[1,2],[3,4])
#print(ary)


#Way-1

a = numpy.array([1,2,3,4,5])
print(a)
print(a.dtype)
a = numpy.array([1,2,3,4,5],int)
print(a)
print(a.dtype)
a = numpy.array([1,2,3,4,5],float)
print(a)
print(a.dtype)
a = numpy.array([1,2,3,4,5.6])
print(a)
print(a.dtype)


#Way-2
#default 50 parts
a = numpy.linspace(1,5);
print(a)
print(len(a))


#Way-3
a = numpy.arange(2,20,2)
print(a)
print(a.dtype)
print(len(a))

#Way-4

a =numpy.logspace(1,40,5)
print(a)
print(a.dtype)
print('%.2f' %a[0])
print('%.2f' %a[1])
print('%.2f' %a[2])
print('%.2f' %a[3])
print('%.2f' %a[4])


#efficient ways 5 and 6
ary=numpy.zeros(5)
print(ary)
ary=numpy.zeros(5,int)
print(ary)

ary=numpy.ones(10)
print(ary)
ary=numpy.ones(10,int)
print(ary)



