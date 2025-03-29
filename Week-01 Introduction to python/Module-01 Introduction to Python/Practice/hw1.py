# How to get array element with index.

friends = ['nazmul', 'alamin', 'shakirul', 'arifin', 'shahed']
# for index, friend in enumerate(friends):
for index, friend in enumerate(friends, 1):
    print(f'Index: {index}, Element: {friend}')