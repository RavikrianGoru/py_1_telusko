# encoding=utf-8
# When data is sent over the Internet, we need to send it in bytes... something your computer easily understands.
# The rules for translating Unicode (which is what Python uses when it stores a string) to bytes is called encoding.
# A popular encoding to use is UTF-8.

import io

def main():
    print('We need to put # encoding=utf-8 as comment in this file as python has to know which encoding to use')
    f = io.open('abc.txt', 'wt', encoding='utf-8')
    f.write(u'This is text data in unicode format. it can be non-english chars')
    f.close()

    f = io.open('abc.txt', encoding='utf-8')
    text = f.read()
    print(text)
    f.close()


if __name__ == '__main__':
    main()