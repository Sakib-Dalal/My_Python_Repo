s = {1: 10, 2: 20, 3: 30, 4: 40}
x = {}
for i, j in reversed(s.items()):
    print(i, j)
    x[i] = j
print(x)
