def fun(x, y, z):
    return x + y, y + z, x / y, round(y / z, 2)


s = fun(1, 2, 3)
print(s)
print(type(s))


def fun2(x, y, z):
    return [x, y, z]


s = fun2("Hello", "World", "!")
print(s)
print(type(s))


def fun3(x, y, z):
    return {x, y, x}


s = fun3("Hello", "World", "!")
print(s)
print(type(s))


def fun4(x, y, z, a):
    return {x: y, z: a}


s = fun4("A", 1, "B", 2)
print(s)
print(type(s))
