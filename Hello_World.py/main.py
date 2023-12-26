d = {"a": 1, "b": 2, "c": 3, "d": 4}

d1 = {i: j**3 for (i, j) in d.items()}
print(d1)

d2 = {i: j**3 for (i, j) in d.items() if j > 3}
print(d2)

g = {1: 2, 3: 4}
print(g[3])

d3 = {i: ("Even" if j % 2 == 0 else "Odd") for (i, j) in d.items()}
print(d3)


