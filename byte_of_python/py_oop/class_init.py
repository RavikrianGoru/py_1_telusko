class Person:
    def __init__(self, name):# we can give any name instead of self but recommended to use self.
        self.name =name

    def say_hi(self):
        print(f'{self.name} : Hi all')

    def say_bye(anyName):
        print(f'{anyName.name} : Bye all')

#p = Person() # TypeError: __init__() missing 1 required positional argument: 'name'
p = Person('Ravi')
p.say_hi()
p.say_bye()