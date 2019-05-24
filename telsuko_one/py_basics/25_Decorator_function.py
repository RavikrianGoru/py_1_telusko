# Consider this div function is available in some other file and can not edit by us.
def div(a, b):
    #if a < b:
    #    a,b=b,a
    print(a/b)


def smart_div(func):
    def inner_func(a,b):
        if a < b:
            a,b=b,a
        return func(a,b)
    return inner_func

div = smart_div(div)

div(4,2)
div(2,10) # 1st argument < 2nd arg