# Take 3 numbers from the user and give me the largest numbers as output
x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")
z = input("Enter 3rd number: ")

num1 = int(x)
num2 = int(y)
num3 = int(z)

if num1 >= num2 and num1 >= num3:
    print(num1, "is large")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is large")
else:
    print(num3, "is large")