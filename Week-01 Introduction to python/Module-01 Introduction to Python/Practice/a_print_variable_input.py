# print
print("Hello Python Programming")
print('Our journey is begin from today')

# variable: variable_name = value
name = 'Raisul Islam'
age = 22
height = 5.6
weight = 49.750
is_single = True
is_healthy = False

print('Name:', name)
print('Age:', age)
print('Height:', height)
print('Weight:', weight)
print('Single:', is_single)
print('Healthy:', is_healthy)
print(height + weight)

# type
print(type(name))
print(type(age))
print(type(height))
print(type(is_single))

print('Hi, I am' + ' ' + 'Raisul Islam')
text = f"Let introduce {name}, age {age}, height {height}"
print(text)

# input
monthly_salary = input('Tell me your monthly salary: ')
# print('Ok, your monthly salary is:', monthly_salary)
# print(type(monthly_income))
monthly_kpi = input('Tell me your monthly kpi: ')
# print("Ok, your monthly total income is:", monthly_salary + monthly_kpi)
print("Ok, your monthly total income is:", int(monthly_salary) + int(monthly_kpi))
