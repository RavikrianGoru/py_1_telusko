#  Acquiring a resource in the try block and subsequently releasing the resource in the finally block is a common pattern.
# Hence, there is also a with statement that enables this to be done in a clean manner:
# we are using the open function with the with statement - we leave the closing of the file to be
# done automatically by with open.


def main():
    with open('abc.txt') as f:
        #thefile.__enter__
        for line in f:
            print(line, end='')
        #thefile.__exit__


if __name__ == '__main__':
    main()