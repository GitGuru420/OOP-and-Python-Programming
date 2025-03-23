""" 
Take a string as input and count the number of vowels (a, e, i, o, u) in it. 
"""
st = input('Enter a string: ')
count = 0
for s in st:
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
        count += 1
print(count)