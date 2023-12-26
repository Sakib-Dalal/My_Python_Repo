a = [(i, j, k) for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3] if i != j and j != k and k != i]
print(a)