#1 len,index,count methods
s = 'Goru RaviKiran Goru'
print(s)
print('len(s):', len(s))
print('Count a substr or char:', s.count('i'))
print('Count a substr or char:', s.count('Goru'))
print(s.index('Go'))
print(s.index('Go',3))


# Slice operator s = 'Goru RaviKiran Goru'
# s[begin:end] end is exclusion
print(s[0:len(s)])
print(s[0:4])
print(s[0:])
print(s[:len(s)])
print(s[:])

print(s[5:1000])
print(s[10:3]) #nothing prints
print(s[10:3:-1]) #nothing prints


# Str arthmetic oerations
s = 'ravi' + 'kiran'
s = 'ravi' * 3
s = 4 * 'ravi' * 2
print(s)
# s = 'ravi' * 'kiran' #TypeError can not multiply sequence by non-int of tye str.
# s = 'ravi' + 3 #TypeError: can only concatenate str (not "int") to str

