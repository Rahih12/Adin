import math

m = float(input('Введите a: '))
n = float(input('Введите n: '))

z1 = m + 2 / math.sqrt(2 * m) - m / math.sqrt(2 * m) + 2 + 2 / m - math.sqrt(2 * m) * math.sqrt(m) - math.sqrt(2) / m + 2
z2 = 1 / math.sqrt(m) * math.sqrt(2)

print("z1 =", z1)
print("z2 =", z2)
