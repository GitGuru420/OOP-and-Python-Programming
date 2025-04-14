# Operators: +, -, *, %, /, //, **
x = input("Enter a number: ")
y = input("Enter another number: ")
num1 = int(x)
num2 = int(y)

print(f"Sum of {x} and {y} = {num1 + num2}")
print(f"Sub of {x} and {y} = {num1 - num2}")
print(f"Mul of {x} and {y} = {num1 * num2}")
print(f"Mod of {x} and {y} = {num1 % num2}")
print(f"Div of {x} and {y} = {num1 / num2}")
print(f"Floor Div of {x} and {y} = {num1 // num2}")
print(f"Power of {x} and {y} = {num1 ** num2}")

# Comparison Operators: >, <, >=, <=, ==, !=
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

# Assignment Operators: +=, -=, *=, /=
# x = x + y
x += y
print(x)