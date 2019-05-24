
def top10Sqr():
    i = 1
    while i <= 10:
        yield i * i
        i+=1

vals = top10Sqr()

for i in vals:
    print(i)

