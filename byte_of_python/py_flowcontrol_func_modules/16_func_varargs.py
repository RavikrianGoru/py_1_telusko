# Sometimes we need to pass n=any number of items to function: then varArgs required
# *param1 is tuple
# **param2 is dictionary

def total(a=5, *numbers, **phonebook):
    print(f'a = {a}')

    # iterate through all the items in tuple
    for each in numbers:
        print(f'Item from numbers: {each}')

    # iterate though all the items in dictionary
    for eachKey, eachValue in  phonebook.items():
        print(f'{eachKey} {eachValue}')

total(1,10,20,30,40,50,ram=100,raj=200,rani=300)