def full_name(first, last):
    name = f'{first} {last}'
    return name

# take parameters in order (serial wise)
# name = full_name('Ali', 'Kodom')
name = full_name(last = 'Kodom', first = 'Ali')
print(name)

def famous_name(first, last, title, **addition):
    name = f'{title} {first} {last}'
    # print(addition)
    # print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name
name = famous_name(first='Ali', last='Kodom', title='Hujur', addition='Shayekh')
print(name)


# return multiple things from an array
def a_lot(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    remain = num1 - num2
    # return sum, mul, remain
    return [sum, mul, remain]
everything = a_lot(55, 21)
print(everything)