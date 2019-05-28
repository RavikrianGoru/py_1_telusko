import sys
import time


def main():
    f = None
    try:
        print("-----Resource creation logic-----")
        f = open('abc.txt', 'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
                # Not closed file here. Who will rclose the opened file
            print(line, end='')
            sys.stdout.flush()
            print("Press ctrl+c now")
            time.sleep(2) # wait for sometime
    except IOError:
        print('abc.txt is not available ')
    except KeyboardInterrupt:
        print('Reading file content is cancelled')
    finally:
        if f:
            print('-----Resource cleanup-----')
            f.close()
        print('Resource closing logic comes here')
    print('All is done')


if __name__ == '__main__':
    main()