
def read_writ_normal_file():
    f1 =None
    f2 =None
    try:
        f1 = open('sample.txt', 'r')
        f2 = open('sample1.txt','w')
        for i in f1:
            f2.write(i)
    except Exception as e:
        print("Exception while readinf/writing file",e)
    finally:
        try:
            f1.close()
        except Exception as e1:
            print('Error while closing file', e1)
        try:
            f2.close()
        except Exception as e1:
            print('Error while closing file', e1)


def read_writ_binary_file():
    f1 =None
    f2 =None
    try:
        f1 = open('MrBean1.png', 'rb')
        f2 = open('MrBean.png','wb')
        for i in f1:
            f2.write(i)
    except Exception as e:
        print("Exception while readinf/writing file",e)
    finally:
        try:
            f1.close()
        except Exception as e1:
            print('Error while closing file', e1)
        try:
            f2.close()
        except Exception as e1:
            print('Error while closing file', e1)


if __name__ =='__main__':
    read_writ_normal_file()
    read_writ_binary_file()
