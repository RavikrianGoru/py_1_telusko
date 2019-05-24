stock = 5
order = int(input("Enter number of items for order"))

i = 1
while i <= order:
    if i > stock:
        print("out of order")
        break
    print("item ",i)
    i += 1
print("Bye")

