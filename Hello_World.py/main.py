# position argument

def fun1(i, j, k):
    print(i + j)
    print(k.upper())


fun1(13, 3.14, "Hello")


# keyword argument

def fun2(i, f, str):
    print(i, f, str)


fun2(12, 13.2, 'Hello')
fun2(i=12, f=13.2, str='Hello')
fun2(str='Hello', i=12, f=13.2)
fun2(f=13.2, str='Hello', i=12)

fun2(12, f=13.2, str='Hello')
fun2(12, str='Hello', f=13.2)


# if number of parameters in a function are unknown
# variable length position
def fun3(*args):
    print()
    for v in args:
        print(v, end=" ")


fun3(3)
fun3("Hello", 3, 23, 34.35)


def fun4(*args):
    print()
    for v in args:
        print(v + (v + 1))


fun4(3, 4, 5)


# variable length keyword
# works as a dictionary
def print_it(**kwargs):
    print()
    for key, value in kwargs.items():
        print(key, value, end=" ")


print_it(a=10)
print_it(a=10, b=3)
print_it(a=10, b=3, s="Hello")

dic = {"1": "10", "2": "20", "3": "30", "4": 40}
print_it(**dic)


