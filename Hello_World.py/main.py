i = {1: 30, 2: 40, 3: 70, 4: 20}
print(i)
print(i.items())
print(i.keys())
print(i.values())

for x in i:
    print(x)
for x in i.keys():
    print(x)
for x in i.values():
    print(x)
for x, y in i.items():
    print(x)

for x in i.items():
    print(x)
    print(type(x))

for x in i.items():
    print(x[0])
for x in i.items():
    print(x[1])
