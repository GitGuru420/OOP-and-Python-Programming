# take 3 numbers from the user and give me the largest number as output

a = input("Enter number 1: ")
b = input("Enter number 2: ")
c = input("Enter number 3: ")

x = int(a)
y = int(b)
z = int(c)

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)