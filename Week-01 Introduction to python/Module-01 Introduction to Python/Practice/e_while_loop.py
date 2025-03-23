# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# break
# num = 1
# while num <= 10:
#     if num == 6:
#         break
#     print(num)
#     num += 1

# continue
num = 1
while num <= 10:
    num += 1
    if num % 3 == 0:
        continue
    print(num)