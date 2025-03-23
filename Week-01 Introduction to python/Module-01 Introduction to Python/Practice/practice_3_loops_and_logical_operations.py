""" 
Print the sum of numbers from 1 to 10. 
"""
# sum = 0
# for num in range(1,11):
#     sum += num
# print(sum)


""" 
Print all odd numbers from 1 to 20.
"""
# for num in range(1,20,2):
#     print(num)


""" 
Take a number as input and find all its factors. 
"""
# x = input('Enter a number: ')
# num = int(x)
# for fact in range(1,num+1):
#     if(num % fact == 0):
#         print(fact)


""" 
Take a number as input and determine whether it is a prime number.
"""
# x = input('Enter a number: ')
# num = int(x)
# checkPrime = False
# for i in range(2,num):
#     if(num % i == 0):
#         checkPrime = True
# if checkPrime is True:
#     print('Not prime')
# else:
#     print('Prime')


""" 
Print the first 10 numbers of the Fibonacci series.
"""
n = 10
a, b = 0, 1
print(a, b, end=" ")
for _ in range(n - 2):
    next_number = a + b
    print(next_number, end=" ")
    a, b = b, next_number