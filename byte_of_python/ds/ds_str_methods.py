# Str object name
name = 'RavikiranGoru'
if name.startswith("Ravi"):
    print('Yes, the string start with Ravi')

print("'index', 'find', and 'for str in str: ")
if 'Go' in name:
    print('Yes, The string contains \'Go\'')

if name.find('Go') != -1:
    print('Yes, The string contains \'Go\' ')

if name.index('Go') != -1:
    print('Yes, The string contains \'Go\' ')

delimiter = '_*_'
myNames = ['ravi', 'kiran', 'goru', 'devi']
print('delimiter.join(myNames): ', delimiter.join(myNames))

