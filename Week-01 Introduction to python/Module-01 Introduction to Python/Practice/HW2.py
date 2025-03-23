# take 3 numbers from the user and give me the largest number as output
a = input('Enter first number: ')
b = input('Enter second number: ')
c = input('Enter third number: ')

a_int = int(a)
b_int = int(b)
c_int = int(c)

print('Largest number:',max(a_int, b_int, c_int))