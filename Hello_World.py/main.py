# unpacking list/tuple/set argument

def fun(a, b, c, d):
    print(a, b, c, d)


lst = [1, 2, 3, 4]
tpl = (1, 2, 3, 4)
s = {1, 2, 3, 4}

fun(*lst)
fun(*tpl)
fun(*s)


# using *args
def fun2(*args):
    print()
    for v in args:
        print(v, end=" ")


fun2(*lst)
fun2(*tpl)
fun2(*s)
