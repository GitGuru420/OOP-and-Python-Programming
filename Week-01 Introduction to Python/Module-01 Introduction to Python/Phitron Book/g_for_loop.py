# range(start, stop, step)
# range with only stop argument
"""
for i in range(10):
    print(i)
"""


# range with start and stop arguments
"""
for i in range(5,10):
    print(i)
"""


# range with start, stop ans step arguments
"""
for i in range(5,15,2):
    print(i)
"""

# Print numbers from 1 to 5 using a for loop 
"""
for num in range(1, 6):
    print(num)
"""


# Print numbers from 1 to 10 and classify them as even or odd using a for loop with if-else statement
"""
for num in range(1,11):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
"""

# continue: Print numbers from 1 to 10, skipping even numbers using a for loop with continue statement
"""
for num in range(1,11):
    if num % 2 == 0:
        continue
    print(num)
"""

# break: Print numbers from 1 onwards until reaching a number greater than 5 using a for loop with break statement
"""
for num in range(1,10):
    if num > 5:
        break
    print(num)
"""

# for loop with string
# Iterate over each character in a string 
"""
word = "Python"
for char in word:
    print(char)
"""

# for loop with list
# Iterate over each element in a list 
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)