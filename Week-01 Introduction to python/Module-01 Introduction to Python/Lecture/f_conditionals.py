# in, not, not in, is, is not
# >, <, >=, <=, ==, !=

# a = 7
# a = 2
# a = 4
# if a > 5:
#     print('5 er besi')
#     print('Sotti e 5 er besi')
# elif a > 3:
#     print('olpo boro')
# else:
#     print('5 er choto')


# boss = False
# if boss is True:
#     print("boss re tel daw")
# else:
#     print('bos re tel dio nah')

# boss = False
# if boss is not True:
#     print('bos re tel dio nah')
# else:
#     print("boss re tel daw")

# nested conditions
coin = 'tail'
boss = False
if boss == True:
    print('Yes Boss')
    if coin == 'tail':
        print('Bos, batting')
    else:
        print('Boss, bowling')
else:
    print('No, Boss')