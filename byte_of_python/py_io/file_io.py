from pip._vendor.pyparsing import oneOf

poem = '''Programming is fun When the work is done
if you wanna make your work also fun: use Python!
'''


def write_into_file(fname, mode, data):
    # Open a file with write mode  'w' default mode is read 'r'
    # help(open)
    f1 = open(fname, mode)
    f1.write(data) # write data in to opened file.
    print(f1.name, f1.mode)
    print('Current cursore position', f1.tell())
    print('Move cursore to any plcae by f1.seek(n)')
    f1.close()


def read_from_file(fname, mode):
    # Open a file with write mode  'w' default mode is read 'r'
    f1 = open(fname, mode)
    while True:
        line = f1.readline()
        if len(line) == 0:
            break
        print(line)
    f1.close()


def main():
    write_into_file('file1.txt', 'w', poem)
    read_from_file('file1.txt', 'r')


if __name__=='__main__':
    main()
