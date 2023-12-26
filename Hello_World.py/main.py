a = [n for n in range(2, 51) if n % 2 == 0 and n % 4 == 0]
print(a)

l = []
for i in range(2, 51):
    if i % 2 == 0 and i % 4 == 0:
        l.append(i)
print(l)
