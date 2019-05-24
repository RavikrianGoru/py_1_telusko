from numpy import *

# Add a number to alla the elements of array & updated the array
arr = array([1,2,3,5,7])
print(arr)
arr = arr + 5
print(arr)
print('-----')

# Add two arrays
arr1 = array([2,5,8,9,10])
print(arr)
print(arr1)
arr3 = arr + arr1 # both arrays must be same size
print(arr3)
print('-----')

print(arr1)
print(sin(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))
print(unique(arr1))
a=concatenate([arr1,arr])
print(a)
print('-----')

#copy arrays, but both poit to same address.(aliase)
print('Copy array: by =')
arr4=arr;
print(arr)
print(arr4)
print(id(arr))
print(id(arr4))


#shallow copy
print('Copy array: by view()')
arr4=arr.view();
arr[3]=120
print(arr)
print(arr4)
print(id(arr))
print(id(arr4))

#Deep copy
print('Copy array:by copy()')
arr4=arr.copy();
arr[3]=500
print(arr)
print(arr4)
print(id(arr))
print(id(arr4))





