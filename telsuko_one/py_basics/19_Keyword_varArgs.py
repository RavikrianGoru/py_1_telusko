
def person(name, **data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)


def emp(**data):
    for i,j in data.items():
        print(i,'---',j)

person('Ravi',age=28,city='Guntur',phone=9898565610)
emp(name='ravi',age=30,sal=30,city='gnt')