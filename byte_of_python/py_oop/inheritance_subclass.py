class SchoolMember:
    '''Represents any school memers. base/super class'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Initializing SchoolMember: {self.name}')

    def details(self):
        print(f'Details Name : {self.name}, Age : {self.age}', end=" ")


class Teacher(SchoolMember):
    '''Represents any teacher. child/sub class'''

    def __init__(self, name, age , sal):
        # Python does not automatically call the constructor of the base class. have to call explicitly
        SchoolMember.__init__(self, name, age) # calling base class constructor/__init__
        self.sal = sal
        print(f'Initializing Teacher: {self.name}')

    def details(self):
        SchoolMember.details(self)
        print(f'Salary : {self.sal}', end=" ")

class Student(SchoolMember):
    '''Represents any Student. child/sub'''

    def __init__(self, name, age, marks):
        # Python does not automatically call the constructor of the base class. have to call explicitly
        SchoolMember.__init__(self, name, age) # calling base class constructor/__init__
        self.marks = marks
        print(f'Initializing Student: {self.name}')

    def details(self):
        SchoolMember.details(self)
        print(f'Marks : {self.marks}', end=" ")


def main():
    t1 = Teacher('Mr. Madhu', 35, 35000.00)
    t2 = Teacher('Mss. Lakshmi', 32, 34000.00)
    s1 = Student('Ravi', 26, 75)
    s2 = Student('Kiran', 25, 77)
    s3 = Student('Devi', 24, 79)

    l = [t1,t2,s1,s2,s3]
    for each in l:
        each.details() # this is common method for Teacher and Student
        print()

if __name__ == '__main__':
    main()