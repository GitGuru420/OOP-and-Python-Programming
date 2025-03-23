# arithmetic operators: +, -, *, /, %, //
a = 12
b = 8
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# comparison operators: >, <, >=, <=, ==, !=
# python do not supports ++, -- operator
power = a ** b  # ** power operator
print(power)

# assignment operator: +=, -=, *=, /=
a += b
print(a)

# condition: in, no, not in, is, is not
# logical operator: and, or, not

if a == b:
    print("Khaichi Tore")
elif a < b:
    print("OK, Maf Korlam")
else:
    print("Hala Vaag")

boss = True
if boss is True:
    print('Single')
else:
    print('Mingle')

n1 = 121
n2 = 234
if(n1 % 2 == 1):
    if(n1 > n2 or n1 == n2):
        print('All is Well')
    else:
        print("Not Well")
else:
    print('Mara Khaw')