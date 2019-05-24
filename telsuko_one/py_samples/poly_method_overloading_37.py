class Nums:
    def __init__(self,m=0):
        self.m=m

    #def sum(self, m1,m2):
    #    return m1+m2

    #def sum(self,m1,m2, m3):
    #    return m1+m2+m3

    #method overloading trick
    def sum(self, m1=None, m2=None, m3=None):
        if m1!=None and m2!=None and m3!=None:
            return m1+m2+m3
        elif m1!=None and m2!=None:
            return m1+m2
        elif m1!=None:
            return m1
        else:
            return 0

    # method overloading trick
    def add(self,*a):
        s =0
        for i in a:
            s+=i
        return s




print('--------------------------- \nMethod overloading by defining \n m1(a,b) \n m1(a,b,c) method \ndeclaration does not support in python')
n1 = Nums()
#print(n1.sum(5,10))
#print(n1.sum(5,10,15))

print('n1.sum(5)=', n1.sum(5))
print('n1.sum(5,10)=', n1.sum(5,10))
print('n1.sum(5,10,15)=', n1.sum(5,10,15))

print('n1.add(50)=', n1.add(50))
print('n1.add(50,100)=', n1.add(50,100))
print('n1.add(50,100,150)=', n1.add(50,100,150))

print('--------------------------- \nMethod overriding, same class is available in Parent and child classes')


class A:
    def show(self):
        print(type(self), "show() in A")


class B(A):
    def show(self):
        print(type(self), "show() in B")

obj1 = A()
obj1.show()
obj2 =B()
obj2.show()