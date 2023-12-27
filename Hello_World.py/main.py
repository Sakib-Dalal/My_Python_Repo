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
print()


# for dictionaries using keywords
def fun3(name, marks):
    print(name, marks)


d = {"name": "Sakib", "marks": 50}
fun3(*d)
fun3(**d)


# with multiple values
def fun4(**kwargs):
    print()
    for k, v in kwargs.items():
        print(k, v, end=" ")


my_dic = {"1": 10, "2": 20, "3": 30, "4": 40}
fun4(**my_dic)
