# in, not, not in, is, is not
# >, <, >=, <=, ==, !=
# and, or, not

# a = 7
# a = 2
a = 4
if a > 5:
    print('5 er besi')
    print('koto besi ke jane')
elif a > 3:
    print('3 er besi 5 er kom')
elif a == 2:
    print('dui er soman soman')
else:
    print('5 er choto')

# boss = True
# if boss is True:
#     print('boss re tel daw')
# else:
#     print('boss re dijel daw')

boss = True
if boss is not True:
    print('boss re dijel daw')
else:
    print('boss re tel daw')

# nested conditions
coin = 'head'
if boss == True:
    print('boss you are joss')
    if coin == 'tail':
        print('boss is batting')
    else:
        print('boss is bowling')
else:
    print('you are loss not a boss')

if 8%2 == 0 and 5%2==1:
    print('do something')
else:
    print('do not something')