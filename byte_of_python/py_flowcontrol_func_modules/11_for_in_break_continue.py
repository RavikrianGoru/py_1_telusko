# for..in is another looping statement. whic iterates over a sequence of objects.
for i in range(1, 20):
    if i > 10:
        break
    elif i % 2 != 0:
        continue
    else:
        print(i, end="")
    print("-", end="")
else:
    print("for loop is over")

print('\nlist(range(0,11,2) :', list(range(0,11,2)))