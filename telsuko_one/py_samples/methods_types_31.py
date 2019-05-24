
class Student:
    school = "SJRMM"

    def __init__(self,rno,name,m1=35,m2=35,m3=35,m4=35,m5=35,m6=35): # constructor
        self.rno=rno
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.m6=m6

    # instance methods- accessor
    def get_rno(self):
        return self.rno

    # instance methods- mutator
    def set_rno(self,value):
        self.rno = value

    def avg(self):
        return (self.m1+self.m2+self.m3+self.m4+self.m5+self.m6)/6

    def print_student(self):
        print(self.rno, self.name, self.m1, self.m2, self.m3, self.m4, self.m5, self.m6)

    # class method
    @classmethod
    def getSchool(cls):
        return cls.school

    # static method
    @staticmethod
    def info():
        print("This is student class- static method, is nothing to do with class/instance variables.")


s1 =Student(10,'ravikiran',50,60,40,50,65,70)
s2 =Student(10,'ravikiran')
s2.print_student()
s2.set_rno(50)
s2.print_student()



print(s1.avg())
print(s2.avg())

print(Student.getSchool())

Student.info()