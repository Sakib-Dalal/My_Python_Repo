s = {
    "a": {1: 10, 2: 20},
    "b": {3: 30, 4: 40},
    "c": {5: 50, 6: 60}
}
print(s)
for i, j in s.items():
    print(i, j)
for i, j in s["a"].items():
    print(i, j)
for i, j in s["c"].items():
    print(i, j)
    