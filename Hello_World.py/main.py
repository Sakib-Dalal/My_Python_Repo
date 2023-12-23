s = {1: 10, 2: 20, 3: 30, 4: 40}
p = {5: 50, 6: 60, 7: 70, 8: 80}

print(s.get(3, "Absent"))
print(s.get(5, "absent"))
print(s)
print(s[2])

print(s.pop(1))
print(s)
print(s.popitem())
print(s)
print(s.update(p))
print(s)
