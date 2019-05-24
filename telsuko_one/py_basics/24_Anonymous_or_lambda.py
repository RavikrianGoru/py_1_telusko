
f = lambda a: a*a
m = lambda a,b: a*b
n = lambda a,b,c: a*b*c

print("Square Lambda:", f(5))
print("Multiplication of 2 numbers by Lambda:", m(5,6))
a = 10
b = 5
c = 2
print("Multiplication of {} {} {}:".format(a,b,c), n(a,b,c))