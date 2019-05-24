# Binary search, items must be sorted.

index = -1
def binary_search(items,item):
    l = 0
    u = len(items) - 1
    while l <= u:
        m = (l+u) // 2
        if items[m] == item:
            globals()['index'] = m
            return True
        else:
            if items[m] < item:
                l = m + 1
            else:
                u = m - 1
    else:
        return False

items = [1,4,7,9,13,17]
item = 4

if binary_search(items, item):
    print('Item found at {} index'.format(index))
else:
    print('Item not found')
