#Bubble sort
def bubble_sort(items):
    for i in range(len(items)-1, 0 , -1):
        for j in range(i):
            if items[j] > items[j+1]:
                items[j],items[j+1]=items[j+1],items[j]
    return items

items = [4, 5, 3, 1 ,78, 24,56,56,2]

print(bubble_sort(items))