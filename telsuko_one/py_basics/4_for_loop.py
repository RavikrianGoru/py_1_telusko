x = [1, "ravi", 5.8]
print(x)

print("for is used for list")
x = [1, "ravi", 5.8]
for i in x:
    print(i)

print("for is used for tuple")
x = (1, "ravi", 5.8)
for i in x:
    print(i)

print("for is used for set")
x = {1, "ravi", 5.8}
for i in x:
    print(i)

print("for is used for string")
y = "Ravikiran"
for i in y:
    print(i)

print("for is used for range")
for i in range(1, 5):
    print(i)


for i in range(2, 10, 2):
    print(i)

print("No multiples of 5")
for i in range(10, 0, -1):
    if i % 5 != 0:
        print(i)
