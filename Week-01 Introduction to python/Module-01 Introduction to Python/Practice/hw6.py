# grade calculator in python (if, elif, else)

marks = input('Enter marks: ')
mark = int(marks)

if mark >= 90:
    print('A+')
elif mark >= 80:
    print('A')
elif mark >= 70:
    print('A-')
elif mark >= 60:
    print('B')
elif mark >= 50:
    print('C')
elif mark >= 33:
    print('D')
else:
    print('Fail')