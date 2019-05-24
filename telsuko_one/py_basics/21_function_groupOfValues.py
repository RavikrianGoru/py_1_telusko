
def count_even_odd(lst):
    e = 0
    o = 0
    for i in lst:
        if i % 2 == 0:
            e+=1
        else:
            o+=1
    return e,o
# Count the number of even numbers and odd numbers
lst = [2,53,68,24,67,96,33,55,75,22,57,43,11,467,87]
print(lst)
even,odd=count_even_odd(lst)
print("Event cout : {} Odd count : {}".format(even,odd))




def getNames():
    count = int(input("Enter no of names:"))
    for i in range(count):
        name = input("Enter name: ")
        if len(name) >= 5:
            print(name)

# Get user names and print name if length of name is 5 or more
getNames()
