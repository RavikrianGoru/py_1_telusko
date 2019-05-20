# Lists, tuples and strings are examples of sequences
# Features: Membership test 'in', 'not in' expression
#            Indexing operations
#            slicing operations

l = [1,2,1,3,4]
s = 'raviG'

# Indexing or 'Subscription' operation #
print(f'item 0 = {l[0]}')
print(f'item -1 = {l[-1]}')
print(f'char at 0 = {s[0]}')
print(f'char at -1 = {s[-1]}')

# Slicing on a list #
print(f'item 0 to 3,  l[0:3] = {l[0:3]}')
print(f'item 0 to end, l[0:] = {l[0:]}')
print(f'item 0 to -1(end -1), l[0:-1] = {l[0:-1]}')
print(f'item 0 to end, l[0:100] = {l[0:100]}')
print(f'item 0 to end, l[:] = {l[:]}')

print('characters 1 to 3 is', s[1:3])
print('characters 2 to end is', s[2:])
print('characters 1 to -1 is', s[1:-1])
print('characters start to end is', s[:])

shoplist = ['apple', 'mango', 'carrot', 'banana']
print('shoplist ', shoplist)
print('shoplist[::1] ', shoplist[::1])
print('shoplist[::3] ', shoplist[::3])
print('shoplist[::-1] ', shoplist[::-1]) #reverse order



