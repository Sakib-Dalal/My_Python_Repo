def cal_sum_prod(x, y, z):
    ss = x + y + z
    pp = x * y * z
    return ss, pp


a = int(input("Enter a num: "))
b = int(input("Enter b num: "))
c = int(input("Enter c num: "))

s, p = cal_sum_prod(a, b, c)
print(s, p)
