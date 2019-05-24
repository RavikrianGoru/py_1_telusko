# import sys

# if statement
x = int(input("Enter number"))
if x % 2 == 0:
    print("Even number", x)

# if else statement
x = int(input("Enter number"))
if x % 2 ==0:
    print(x, " is even number")
else:
    print(x, " is Odd number")

# if elif else statement
x = int(input("Enter number"))
if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
elif x == 4:
    print("Four")
elif x == 5:
    print("Five")
else:
    print("Wrong input")

# nested if

x = int(input("Enter number:"))
if (x % 2) == 0:
    print("Given number is even:")
    if x>5:
        print("Square of given number:", pow(x, 2))
    else:
        print("Cube of given number:", pow(x, 3))
else:
    print("Given number is odd")



print("bye")