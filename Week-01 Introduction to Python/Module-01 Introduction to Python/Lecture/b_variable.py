age = 45
interest_rate = 2.5
name = "Raisul Islam"
district = "Barisal"
is_single = True
is_sleeping = False


print(age)
print(district)
print(age + interest_rate)


print(type(age))
# Ctrl + / : single line of comment
# print(type(interest_rate))
print(type(district))
print(type(is_single))

# Alt + Shift + A : doc string or multi line comment
""" 
print(type(district))
print(type(is_single)) 
"""

print("Tushar" + " " + "Rahman")
# f string
fname = "Tushar"
lname = "Rahman"
text = f"Hello, My name is {fname} {lname} and age is {age} years. Interesting with rate {interest_rate}%."
print(text)