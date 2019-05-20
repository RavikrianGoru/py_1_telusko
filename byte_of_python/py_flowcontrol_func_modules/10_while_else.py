# while-else
# input() is builtin function. we supply input as string. Once we enter something and press kbd[enter] key.
# input() function returns what we entered as string.
# then we can convert into any format what we required.

pass_mark = 45
running = True

print('Process is started')

while running:
    marks = int(input("Enter marks:"))
    if marks == pass_mark:
        print('you just passed')
    elif marks < pass_mark:
        print('you failed')
        running = bool(int(input("Enter your option(1/0)")))
        print(type(running), running)
    else:
        print("you passed")
else:
    print("While is is completed")

print('Process is completed')



