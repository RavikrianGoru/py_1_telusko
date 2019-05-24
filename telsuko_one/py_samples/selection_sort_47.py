# Selection sort better than bubble sort

def selection_sort(items):
    for i in range(len(items)-1):
        minpos = i
        flag = False
        for j in range(i+1,len(items)):
                if items[j]<items[minpos]:
                    minpos = j
                    flag = True
        if flag:
            items[minpos],items[i] = items[i],items[minpos]
    return items

items = [4, 5, 3, 1 ,78, 24,56,56,2]
print(selection_sort(items))