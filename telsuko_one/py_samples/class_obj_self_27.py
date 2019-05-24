
def check_types():
    a = 10
    print("Type od 10:", type(a))
    b = 'ravi'
    print("Type of \'ravi\'", type(b))


class Computer:  # class Computer

    def __init__(self):  # constructor with out args
        print("Computer __init__ or constructor",self)

    def config(self):     # method without args
        print("config() : i5 16gb 1TB")


def check_computer():
    comp0 = Computer()
    comp1 = Computer()

    # Way-1
    Computer.config(comp0)
    Computer.config(comp1)

    # Way-2
    comp0.config()
    comp1.config()


class Emp:

    def __init__(self,id,name,age,sal):    # constructor with args
        print("Emp __init__ or constructor",self)
        self.id=id
        self.name=name
        self.age=age
        self.sal=sal

    def get_emp(self):
        print("id = {}".format(self.id))
        print("name = {}".format(self.name))
        print("age = {}".format(self.age))
        print("sal = {}".format(self.sal))


def check_emp():
    emp1 = Emp(10,'ravi',25,30)
    emp1.get_emp()


# start point of execution
if __name__ == '__main__':
    check_types()
    check_computer()
    check_emp()
