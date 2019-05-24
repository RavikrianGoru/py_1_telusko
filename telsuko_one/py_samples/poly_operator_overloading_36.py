
a = 10
b = 5
print(a+b)
print(int.__add__(a,b))

s1 ='Ravi'
s2 ='Goru'

print(s1+s2)
print(str.__add__(s1,s2))

print(a)
print(a.__str__())


class Student:
    def __init__(self,name,m1,m2):
        self.name=name
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        return Student(self.name+other.name, self.m1+other.m1, self.m2+other.m2)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.m1, self.m2)


s1 = Student('ravi', 59, 62)
s2 = Student('kiran', 63, 73)

print("s1 :", s1)
print('s2 : ', s2)
print("s1 + s2: ", s1+s2)


class Student1:
    def __init__(self,name,m1,m2):
        self.name=name
        self.m1=m1
        self.m2=m2


s1 = Student1('ravi', 59, 62)
s2 = Student1('kiran', 63, 73)

print("S1 : ", s1)
print("S2 : ", s2)
print("S1 + S2: ", s1+s2)


