a = [n for n in range(2, 51) if n % 2 == 0 and n % 4 == 0]
print(a)

l = []
for i in range(2, 51):
    if i % 2 == 0 and i % 4 == 0:
        l.append(i)
print(l)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [i for j in mat for i in j]
print(a)

a = [*mat[0], *mat[1], *mat[2]]
print(a)
