class ShortNameException(Exception):
    '''This is user defined Exception class which must be sub class of Exception'''
    def __init__(self, lenght, atleast):
        Exception.__init__(self)
        self.length = lenght
        self.atleast = atleast


class InvalidAgeException(Exception):
    def __init__(self, age,minage):
        Exception.__init__(self)
        self.age = age
        self.minage = minage


try:
    name = input('Enter name:')
    if len(name) < 3:
        raise ShortNameException(len(name),3)
    age = int(input('Enter age:'))
    if age < 18:
        raise InvalidAgeException(age, 18)
except EOFError:
    print('Why did you enter End Of File?')
except ShortNameException as ex:
    print(f'{name} should be at least {ex.atleast} chars but it has {ex.length}?')
except InvalidAgeException as ex:
    print(f'Given age {ex.age} should be at least {ex.minage}?')
