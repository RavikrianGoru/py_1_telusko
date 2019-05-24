# r = int(input("Enter nuober of rows"))
# c = int(input("Enter number of columns"))

for r in range(4):
    for c in range(4):
        print("* ", end="")
    print()
print("--------")

for r in range(4):
    for c in range(r+1):
        print("* ", end="")
    print()
print("--------")

for r in range(4, 0, -1):
    for c in range(r):
        print("* ", end="")
    print()
print("--------")

for r in range(4):
    for c in range(4-r):
        print("* ", end="")
    print()
print("--------")


for i in range(1, 5):
    for j in range(i, 5):
        print(j, end=" ")
    print()

print("--------")
for i in range(4):
    for j in range(4):
        if j<=i:
            print(chr(65+j),end=" ")
        else:
            print(chr(65+j+14),end=" ")
    print()
print("--------")
