"""  
num = 1
# while num < 10:
while num <= 10:
    print(num)
    num += 1
"""

# break
"""  
num = 1
while num <= 10:
    print(num)
    num += 1
    if num == 5:
        break
"""

# continue
"""  
num = 1
while num <= 10:
    if num == 5:
        continue
    print(num)
    num += 1
"""

"""  
num = 1
while num <= 10:
    num += 1
    if num == 5:
        continue
    print(num)
"""

num = 0
while num <= 10:
    num += 1
    if num % 2 == 1:
        continue
    print(num)