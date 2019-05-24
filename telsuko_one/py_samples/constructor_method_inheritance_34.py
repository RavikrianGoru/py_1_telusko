
class A:

    def __init__(self):
        print('__init__ of A')
    def f1(self):
        print("f1() of A")

    def f2(self):
        print("f2() of A")

class B(A):

    def f1(self):
        print("f1() of B")

    def f3(self):
        print("f3() of B")

print('A obj is created')
a =A()
a.f1()
a.f2()
print('B obj is created')
b =B() # it internally calls __init__ of A as B does not have __init__() in B
b.f1()
b.f2()
b.f3()

class S:

    def __init__(self):
        print('__init__ of S')
    def f1(self):
        print("f1() of S")

    def f2(self):
        print("f2() of S")

class T(S):

    def __init__(self):
        print("__init__ of T")
    def f1(self):
        print("f1() of T")

    def f3(self):
        print("f3() of T")

print('S obj is created')
s =S()
s.f1()
s.f2()
print('T obj is created')
t =T() # it calls __init_ of T itself.
t.f1()
t.f2()
t.f3()


class X:

    def __init__(self):
        print('__init__ of X')
    def f1(self):
        print("f1() of X")

    def f2(self):
        print("f2() of X")

class Y:

    def __init__(self):
        print("__init__ of Y")
    def f1(self):
        print("f1() of Y")

    def f3(self):
        print("f3() of Y")

class Z(X,Y):

    def __init__(self):
        super().__init__()
        print("__init__ of Z")
    def f(self):
        super().f1()
        print("f() of Z")


z =Z() # it calls __init__ of X as per MRO
z.f1()
z.f()