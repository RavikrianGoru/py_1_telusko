r = range(10)
print(type(r), r)
print('start {} step {} stop {}'.format(r.start, r.step, r.stop))
for each in r:
    print(each, end=" ")
print(2 * '\n')


print(r[0])
print(r[2])
print(r[-1])
print(r[0:])
# r[1] = 1000 TypeError: 'range' object does not support item assignment


for each in r[1:5]:
    print(each,end=" ")
print(2 * '\n')

r1 = range(5, 10)
print(type(r1), r1)
print('start {} step {} stop {}'.format(r1.start, r1.step, r1.stop))
for each in r1:
    print(each, end=" ")
print(2 * '\n')


r2 = range(20, 0, -2)
print(type(r2), r2)
print('start {} step {} stop {}'.format(r2.start, r2.step, r2.stop))
for each in r2:
    print(each, end=" ")
