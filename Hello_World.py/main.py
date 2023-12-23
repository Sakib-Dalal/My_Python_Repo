s1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
s2 = {6: 60, 7: 70, 8: 80, 9: 90, 10: 100}
# doesnt work print(s1 + s2)
# doesnt work s3 = {1: 10} + s2

# cloning
s3 = s1
print(s3)

print(1 in s1)
print(10 in s1.values())
print(s1 is s2)
print(s1 is s3)

# aliasing is normally adding
s1[0] = 10
print(s1)
