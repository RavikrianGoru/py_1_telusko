class Computer:
    def __init__(self):
        self.name = 'ravi'
        self.age = 28

    def update(self):
        self.name = "RAVI"
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            print("Same ages")
        else:
            print("Different ages")

def main():
    comp1 = Computer()
    comp2 = Computer()

    comp1.update()
    #comp2.update()
    print(comp1.name)
    print(comp2.name)

    comp1.compare(comp2)

if __name__ == '__main__':
    main()