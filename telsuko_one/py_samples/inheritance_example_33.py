# single-level
class A:
    def m1(self):
        print("A--m1()")
    def m2(self):
        print("A--m2()")

class B(A):
    def m3(self):
        print("B--m3()")
    def m4(self):
        print("B--m4()")


# multi-vel
class A1:
    def m11(self):
        print("A1--m11()")
    def m22(self):
        print("A1--m22()")

class B1(A1):
    def m33(self):
        print("B1--m33()")
    def m44(self):
        print("B1--m44()")

class C1(B1):
    def m55(self):
        print("C1--m55()")
    def m66(self):
        print("C1--m66()")

# multiple
class X:
    def f1(self):
        print('X--f1()')

class Y:
    def f2(self):
        print('Y--f2()')

class Z(X,Y):
    def f3(self):
        print('Z--f3()')

print('A obj created----')
a =A()
a.m1()
a.m2()

print('B obj created single-level inheritance')
b =B()
b.m1()
b.m2()
b.m3()
b.m4()

print('C1 obj created multi-level inheritance')
c =C1()
c.m11()
c.m22()
c.m33()
c.m44()
c.m55()
c.m66()

print('Z object created multiple inheritance')
z =Z()
z.f1()
z.f2()
z.f3()