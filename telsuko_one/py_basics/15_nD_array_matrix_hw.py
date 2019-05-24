import numpy

m1 = numpy.array([
    [1,2,3],
    [2,4,6]
])

m2 = numpy.array([
    [1,2],
    [2,4],
    [1,2]
])
print('1st Array:', '\n', m1)
print('2nd Array:', '\n', m2)

r1 = m1.shape[0]
c1 = m1.shape[1]
r2 = m2.shape[0]
c2 = m2.shape[1]

if c1 == r2:
    print('m1 * m2 is applicable')
    m = numpy.zeros((r1,c2),int)
    for i in range(r1):
        for j in range(c2):
            temp=0
            for a in range(c1):
                temp+=(m1[i,a] * m2[a,j])
            m[i,j] = temp
    print(m)
else:
    print('m1 * m2 is not applicable')
