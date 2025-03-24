numbers = [12, 45, 98, 68, 10, 21, 34, 55]
odds = []
for num in numbers:
    # if num % 2 == 1:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)

# shortcut
# odd_nums = [num for num in numbers if num % 2 == 1]
odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_nums)

players = ['tamim', 'shamim', 'razzak']
ages = [39, 27, 43]

age_comb = []
for player in players:
    print('player', player)
    for age in ages:
        print(player, age)
        age_comb.append([player, age])
print(age_comb)