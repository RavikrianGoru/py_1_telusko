# There are three flow control statements
# 1) if-elif-else
# 2) for
# 3) while

age = 18

user_input = int(input('Enter age :'))

print("Process is started")
if user_input == age:
    print('You are eligible with conditions')
elif user_input < age:
    print('You are not eligible:')
else:
    print('Yur are eligible with no conditions')
print("Process is completed")