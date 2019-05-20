# When you create an object and assign it to a variable, the variable only refers to the object
# and does not represent the object itself!

# That is, the variable name points to that part of your computer's memory where the object is stored.

# This is called binding the name to the object.

obj1 = [1,2,3,4,5] # one obj
obj2 = [1,2,3,4,5] # new obj with same data
obj3 = obj2 # obj3 points to obj2's object only.

print('obj1 ', id(obj1), obj1)
print('obj2 ', id(obj2), obj2)
print('obj3 ', id(obj3), obj3)

obj4 = obj3[:] # copy entire object by slice operation
print('obj4 ', id(obj4), obj4)