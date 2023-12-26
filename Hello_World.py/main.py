# List Comprehensions
import random
a = [random.randint(0, 100) for n in range(20)]
print(a)

# square and cube root from 0 to 10
a = [(x, x**2, x**3) for x in range(10)]
print(a)

# normal example
a = [x for x in range(10)]
print(a)

a = [int(x) for x in ["10", "20", "30", "40", "50"]]
print(a)

# include numbers in list if it is completely divisible by 2
a = [x for x in range(10, 30) if x % 2 == 0]
print(a)

# include n from list a if n is gater than 20
a = [n for n in a if n > 20]
print(a)