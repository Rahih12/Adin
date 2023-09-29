import math

a = float(input('Введите a: '))
z1= ((a + 2)/math.sqrt(2 * a)-((a)/(math.sqrt(2 * a) + 2))+(2)/(a-(math.sqrt(2 * a)))) * ((math.sqrt(a)-math.sqrt(2))/(a + 2))
z2= 1/(math.sqrt(a)+math.sqrt(2))
print("z1 =", z1)
print("z2 =", z2)
