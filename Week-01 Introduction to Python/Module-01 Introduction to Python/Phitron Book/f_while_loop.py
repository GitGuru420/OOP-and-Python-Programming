# Print number from 1 to 5 using a while loop
"""
num = 1
while num <= 5:
    print(num)
    num += 1
"""

# Print numbers from 1 to 10 and classify them as even or odd using a while loop with if-else statement
"""
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
    num += 1
"""

# continue: Print numbers from 1 to 10, skipping even numbers using a while loop with continue statement
"""
num = 1
while num <= 10:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1
"""

# break: Print numbers from 1 onward until reaching a number greater than 5 using a while loop with break satatement 
num = 1
while True:
    # print(num)
    if num > 5:
        break
    print(num)
    num += 1