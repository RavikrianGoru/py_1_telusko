from threading import *
from time import *

class BoyA(Thread):
    def run(self):
        for i in range(0, 5):
            print('A: Hit the boll')
            sleep(0.2)

class BoyB(Thread):
    def run(self):
        for i in range(0, 5):
            print('B: Hit the boll')
            sleep(0.2)


def main():
    t1 = BoyA()
    t2 = BoyB()
    # normal method calls
    t1.run()
    t2.run()

    # thread calls
    t1.start()
    sleep(0.2)
    t2.start()

    #t1.join()
    #t2.join()
    print('bye')

if __name__=='__main__':
    main()