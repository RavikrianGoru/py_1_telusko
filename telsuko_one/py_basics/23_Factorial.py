import sys

def fact(n):
    if n <= 0:
        return 1
    x = 1
    while n > 0 :
        x *= n
        n -=1
    return x


# Recurrsion: A function calls itself. Python default 1000 times recurrion allowed.
def factRec(n):
    if n == 0:
        return 1
    return  n * factRec(n-1)

x =int(input("Enter number:"))

print("Factorial of {} is {}".format(x,fact(x)))

print("\nDefault recursion limit:",sys.getrecursionlimit())
y = int(input("Enter recurrsion limit:"))
sys.setrecursionlimit(y)
print("Updated recurrrion limit:",sys.getrecursionlimit())


print("Factorial by recurrsion:",factRec(x))