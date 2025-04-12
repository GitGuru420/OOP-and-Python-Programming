# print("Now I need money: ")
# input()
# input("Give me some money: ")
# money = input("Give me some money: ")
# print("Here is your money:", money)

first_money = input("first money: ")
second_money = input("second money: ")
print(first_money, second_money)
total = first_money + second_money
print("total money:", total)
print(type(first_money))
# by default the input from user will be string type

# typecasting
first_money_int = int(first_money)
print(type(first_money_int))
second_money_int = int(second_money)
total = first_money_int + second_money_int
print("total money:", total)

"""  
Google Search
1. convert number to string: str
2. convert decimal to number: float
3. python int vs float
"""