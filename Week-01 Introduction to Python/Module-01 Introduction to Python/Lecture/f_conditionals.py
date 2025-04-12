# in, not, not in, is, is not
"""  
# a = 7
# a = 2
a = 4
if a > 5:
    print("5 er besi")
    print("koto besi ke jane")
elif a > 3:
    print("3 er besi, 5 er kom")
else:
    print("5 er choto")
"""

# boss = False
"""  
if boss is True:
    print("Boss re tel dimu")
else:
    print("Boss re tel dimu na")
"""

"""  
if boss is not True:
    print("Boss re tel dimu na")
else:
    print("Boss re tel dimu")
"""

# nested conditions
boss = True
# coin = 'head'
coin = 'tail'
if boss == True:
    print("boss are joss")
    # if coin == 'tail':
    # if coin == 'tail' and 5 > 2:
    if coin == 'tail' or 10 < 5:
        print("batting")
    else:
        print("bowling")
else:
    print("boss are not joss")