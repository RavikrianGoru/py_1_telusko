# Case-1 print all the multiples of 5: It will print all
nums = [1,5,4,2,60,35,78,8]
for num in nums:
    if num % 5 == 0:
        print(num)
print("----------")

# Case-2 print all the multiples of 5: if no element is multiple of 5 then print not found
nums = [1,3,4,2,78,8]
for num in nums:
    if num % 5 ==0:
        print(num)
    else:
        print("not found")
print("----------")

# Case-2 will print not found in multiple times: we have to use for-else break is required

for num in nums:
    if num%5 ==0:
        print(num)
        break
else:
    print("Not Found")

# Same logic with tag and break statements.
tag = True
for num in nums:
    if num%5 ==0:
        print(num)
        tag = False
        break
if tag:
    print("Not found")

