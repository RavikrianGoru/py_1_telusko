import numpy

a = numpy.array([
    [1,0],
    [0,1]
])

print('2d array:','\n',a)

m = numpy.matrix(a)
print('Matrix form of arry:','\n',m)

print("Form matrix from '1,2,3,4 ; 3,4,5,6'")
m1 = numpy.matrix('1,2,3,4 ; 3,4,5,6')
print(m1)

print("Form matrix from '1 2 3 ; 4  3 4 ; 5 6 9'")
m2 = numpy.matrix('1 2 3 ; 4 3 4 ; 5 6 9')
print(m2)

m3 = numpy.matrix('1 0 1 ; 1 2 4 ; 5 2 2')

print("min() element in matrix:", m2.min())
print("max() element in matrix:", m2.max())
print("diagonal() element in matrix:", m2.diagonal())

print('m2 is :', '\n', m2)
print('m3 is :', '\n', m3)
addedM = m2 + m3
print('Matrices addition: m2 + m3','\n', addedM)

mulM = m2 * m3
print('Matrices multiplication: m2 * m3','\n', mulM)

