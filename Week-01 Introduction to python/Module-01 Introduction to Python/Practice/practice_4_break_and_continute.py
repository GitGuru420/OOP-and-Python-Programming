"""  
Print numbers from 1 to 50, but stop the loop when you reach 25.
"""
# for i in range(1,50):
#     if i == 25:
#         break
#     print(i, end=" ")


"""  
Print numbers from 1 to 20, but skip numbers that are divisible by 5.
"""
for i in range(1,21):
    if i % 5 == 0:
        continue
    print(i, end=" ")