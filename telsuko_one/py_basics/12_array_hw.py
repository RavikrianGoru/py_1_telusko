import array
a=array.array('i',[1,4,7,3,2])

# Reverse of array
print("Before reverse: ",a)

start = 0
end = len(a)-1
while start<end:
    a[start],a[end]=a[end],a[start]
    start+=1
    end-=1
print("After reverse:", a)

# Delete an element without using built in functions
b = array.array(a.typecode, (i for i in a if i!= 4))
print(b)
