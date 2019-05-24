# Scope: local and global variables
# how to differentiate local and global variables: global a
# Can we have local and global variables in a function

a = 10
b = 20
c = 30


def fun1():
    print('When you dont have local variable then it refers global variable',id(a))
    print('a in function:', a)

def fun2():
    a = 5
    print('When you have local variable then it refers local variable',id(a))
    print('a in function:', a)

def fun3():
    global a
    a = 15
    print('When you want to access global variables in fun use global keyword', id(a))
    print('a in function:', a)

def fun4():
    print("If you want use global and local variables in function: global()[i]")
    x = globals()['a']
    a = 5
    print(x)
    print(a)

fun1()
fun2()
fun3()
fun4()

print(id(a),'Global variable a:',a)

