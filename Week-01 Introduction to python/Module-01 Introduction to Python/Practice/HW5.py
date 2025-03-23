# grade calculator in python (if elif else)
mark = input('Enter marks: ')
marks = int(mark)
if marks > 90:
    print('A+')
elif marks > 80:
    print('A')
elif marks > 70:
    print('A-')
elif marks > 60:
    print('B')
elif marks > 50:
    print('C')
elif marks > 32:
    print('D')
else:
    print('F')