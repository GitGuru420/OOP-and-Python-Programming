# How to work "float"
x = 3.1416
y = -2.5
z = 1.0
# print(type(y))

a = 5.5
b = 2.3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

num = 100
height = '5.6'
print(float(num))
print(float(height))

print(round(x, 2))
print(round(x, 0))
print(x + a)

from decimal import Decimal
print(Decimal(x) + Decimal(a))

print(isinstance(x, float))