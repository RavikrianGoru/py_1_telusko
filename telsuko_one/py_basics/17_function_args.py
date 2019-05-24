# python there is no pass by value nor pass by reference
# functions pass by value pass by reference

def update(x):
    print("id of x: ", id(x))
    x += 1
    print("id of x after increment: x will point to different address and will not update the actual variable", id(x))
    print(x)

a = 10
print("id of a :", id(a))
update(a)
print("id of a after function call:", id(a))
print(a)


def update_list(lst):
    print("Id of list:",id(lst))
    lst[2]=10
    print("Id of list after update 2nd item:",id(lst))
    print("List in function:", lst)


lst1 =[1,2,3,4,5]
print("id of list:",id(lst1))
print("Before function call:",lst1)
update_list(lst1)
print("id of list:",id(lst1))
print("After function call:",lst1)


