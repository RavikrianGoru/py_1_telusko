from numpy import *

ary= array([
    [1,2],
    [4,6],
    [8,10]
])


print("ary.dtype Type of array:", ary.dtype)
print("ary.ndim Dimension of array:", ary.ndim)
print("ary.shape Shape of array:",ary.shape)



ary1=ary.flatten()
print('flatten() Converts n-dimension array in to 1d array:',ary1)

ary2=ary1.reshape(3,2)
print('reshape(m,n) Converts 1-d array into m*n array:','\n',ary2)

#metrices
