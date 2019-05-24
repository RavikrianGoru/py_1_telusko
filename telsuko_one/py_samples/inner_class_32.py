class Student:

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.ram='16gb'
            self.cpu='i5'
        def show(self):
            print(self.brand,self.cpu,self.ram)

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop() # creating inner class object inside outer class

    def show(self):
        print(self.roll, self.name)
        self.lap.show()


s1 = Student('ravi',100)
s2 = Student('kavi',200)

s1.show()
s2.show()

# creating inner class object out side the outer class
lap1 = Student.Laptop()
lap1.brand='HHP'
lap1.show()