def print_it(i, j, *args, x, y, **kwargs):
    print()
    print(i, j, end=" ")
    for v in args:
        print(v, end=" ")
    print(x, y, end=" ")
    for k, v in kwargs.items():
        print(k, v, end=" ")


print_it(10, 20, x=30, y=40)

print_it(10, 20, 100, 200, x=30, y=40)

print_it(10, 20, 100, 200, a=15, b=30, c=45, x=30, y=40)
