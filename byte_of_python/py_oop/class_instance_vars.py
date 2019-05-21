class Human:

    __count = 0 # private variable can be access indie class or _self reference.

    def __init__(self, name):
        self.name = name
        self.__count +=1

    def say_hi(self):
        print(f'Hi, here {self.name} speaking')


class Robot:
    """ This is Robot class.

    It has class variable __init__ lly to constructor.
    instance methods which takes self reference current object reference
    class metod which takes cls/Class reference
    and docstring for class and docstings for method too"""
    # class variable
    population = 0

    # init/constructor
    def __init__(self, name):
        self.name = name
        print(f'initializing {self.name}')
        Robot.population += 1

    # instance method
    def die(self):
        """ This instance menthod will update population count whenever object die method called.
        It can be accessed by method.__doc__
        """
        print(f'{self.name} dead')
        Robot.population -= 1 # access class variable
        if Robot.population == 0:
            print(f'{self.name} was the last Robot')
        else:
            print(f'There are still {Robot.population} same as {self.__class__.population} robots available')

    # instance method
    def say_hi(self):
        print(f'Hi, here {self.name} speaking...')

    @classmethod # if it missed calling method raises TypeError: how_many() missing 1 required positional argument: 'cls'
    def how_many(cls):
        print(f'Total number of robots are {cls.population}')

    def willSee(cls):
        print(f'Total number of robots are {cls.population}')

def main():
    r1 = Robot('R001')
    print(f'Show docstrings for Robot class {Robot.__doc__}')
    r1.say_hi()
    Robot.how_many()

    r2 = Robot('R002')
    r2.say_hi()
    Robot.how_many()

    r3 = Robot('R003')
    r3.say_hi()
    Robot.how_many()

    r1.die()
    r2.die()
    print(f' Show docstrings for die method {Robot.die.__doc__}')
    Robot.how_many()
    r3.die()

    Robot.how_many()

    h = Human('Ravi')
    h.say_hi()

if __name__ == '__main__':
    main()