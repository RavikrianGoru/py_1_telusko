
def add(a,*b):
    temp = a
    for i in b:
        temp +=i
    return temp


def sum(a,b):
    return a-b


def mul(a,*b):
    result = a * 1
    for i in b:
        result *=i
    return result


def main():
    print("Hello, Welcome to Python")
    print("This is  cal_util:", __name__)
    add(1,2)
    sum(1,3)
    mul(5,29,2,1)


if __name__ == '__main__':
    main()
