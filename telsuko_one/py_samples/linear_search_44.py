index = -1

def search_for(items,item):
    for i in range(0,len(items)):
        if items[i] == item:
            globals()['index'] = i
            return True
    else:
        return False

def search_while(items,item):
    i = 0
    while i<len(items):
        if items[i] == item:
            globals()['index'] = i
            return True
        i += 1
    return False


# Linear Search
items = [84,2,1,44,6,32,54,12,6,9,70]
item = 54
if search_while(items,item):
    print('Item found at {} index and index start from 0'.format(index))
else:
    print('Item not found')
