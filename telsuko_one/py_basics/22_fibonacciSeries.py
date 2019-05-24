# fibonacciSeries
def fib1(n):
    if n <= 0:
        print("Invalid input")
    else:
        if n == 1:
            print(0)
        else :
            a = 0
            b = 1
            print(a)
            print(b)
            for i in range(2,n):
                c = a + b
                a,b = b,c
                print(c)

def fib2(n):
    if n <= 0:
        print("Invalid input")
    else:
        if n == 1:
            print(0)
        else :
            a = 0
            b = 1
            print(a)
            print(b)
            c = a + b
            while c<= n:
                print(c)
                a, b = b, c
                c = a + b


#fib1(10)
fib2(500)
