# num = int(input("Enter positive number: "))
num = 83

num = int(num/2)

for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
            print("Prime")
print("Bye")
