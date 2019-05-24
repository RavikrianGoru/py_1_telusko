class Computer:
    pass


def main():
    a = 10
    b = 10
    # int,float,str are immutable obj[s]
    obj1 = Computer()
    obj2 = Computer()

    print("id of a: ", id(a))
    print("id of b: ", id(b))
    print("id of obj1: ", id(obj1))
    print("id of obj2: ", id(obj2))


if __name__ == '__main__':
    main()
