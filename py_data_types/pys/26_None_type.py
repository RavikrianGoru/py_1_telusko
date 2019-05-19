
a = 10
print(type(a), a)
a = None
print(type(a), a, id(a))
b = None
print(type(b), b, id(b))



def m1():
    print('hello')
    return None

def m2():
    pass

a = m1()
print(type(a), a, id(a))
a = m2()
print(type(a), a, id(a))




