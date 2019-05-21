class Person:
    def __init__(self, name):# we can give any name instead of self but recommended to use self.
        self.name = name

#    def __init__(self, name, age):# we can give any name instead of self but recommended to use self.
#        self.name = name
#        self.age = age

    def say_hi(self):
        print(f'{self.name} : Hi all')

    def say_bye(anyName):
        print(f'{anyName.name} : Bye all')

#p = Person() # TypeError: __init__() missing 1 required positional argument: 'name'
p = Person('Ravi')
p.say_hi()
p.say_bye()

#p1 = Person('Ravi', 32)
#p1.say_hi()
#p1.say_bye()

