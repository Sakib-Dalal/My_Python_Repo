a = {1: 10, 2: 20, 3: 30}
b = {4: 40, 5: 50}
c = {6: 60, 7: 70, 8: 80}

d = {}

for i, j in a.items():
    d[i] = j
for i, j in b.items():
    d[i] = j
for i, j in c.items():
    d[i] = j

print(d)