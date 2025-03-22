# print('Now I need money')
# input()
# input('Give me some mone: ')
# money = input('Give me some mone: ')
# print("here is your money", money)

first_money = input('Kodom Ali, Dosto kichu taka de: ')
second_money = input('Anas Ali, Dosto kichu taka de: ')
print(type(first_money))
# by default the input from user will be string type:
print('money i got from Kodom',first_money, 'and from Anas', second_money)
first_money_int = int(first_money)
print(type(first_money_int))
second_money_int = int(second_money)
print(type(second_money_int))
total = first_money_int + second_money_int
print('total money i got: ', total)

""" 
Google Search
1. convert number to string: str
2. convert decimal number: float
3. python int vs float
"""