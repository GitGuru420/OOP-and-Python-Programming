numbers = [12, 45, 98, 68]
numbers.append(56)
print(numbers)
numbers.insert(2, 71)
print(numbers)
if 98 in numbers:
    numbers.remove(98)
if 8 in numbers:
    numbers.remove(8)
print(numbers)
last = numbers.pop()
print(last, numbers)
index = numbers.index(71)
print(index)
# index = numbers.index(1)
if 1 in numbers:
    index = numbers.index(1)
    print(index)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)