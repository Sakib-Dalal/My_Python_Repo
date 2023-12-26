arr = [[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13]]
b = [i for j in arr for i in j]
print(b)

# OR
a = [*arr[0], *arr[1], *arr[2]]
print(a)

# print 0 to 4 10 times
m = [i for j in range(10) for i in range(5)]
print(m)

