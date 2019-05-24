# Formal arguments
def person(name, age=18):
    print("Name", name)
    print("Age", age)


def sum(a, *b):
    print(a)
    print(b)
    c = a;
    for i in b:
        c +=i
    print(c)


# Actual Arguments 1 Position, 2 Keyword, 3 Default and 4 Variable length

# Position arguments: have to pass values in order/position
person("Ravi",28)

# Keyword arguments: have to pass values with keyword
person(age=28, name="Ravi")
person(name="Ravi", age=28)

# Default arguments: have to pass values else it takes default values
person("RaviG")

# Variable arguments: have to pass values with any size
sum(1,2,3,4,5)