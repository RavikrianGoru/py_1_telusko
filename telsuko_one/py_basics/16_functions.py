# function with out return
def greet():
    print("hello")
    print("Good Morning")


# function with args and return
def add(x, y):
    c = x + y
    return c


# function with args and multiple return values
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


# functions with multiple returns 3 values
def add_sub_diff(x, y):
    a = x + y
    b = x - y
    c = x * y
    return a, b, c


greet()
result1 = add(10, 20)
result2, result3 = add_sub(10, 20)
result4, result5, result6 = add_sub_diff(20, 5)

print(result1)
print(result2, result3)
print(result4, result5, result6)

