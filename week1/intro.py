mark = input('Please enter a your mark and I will tell you your grade: ')

m = int(mark)

if m >= 80:
    print('Your grade is A')
elif m >= 70:
    print('Your grade is B')
elif m >= 60:
    print('Your grade is C')
elif m >= 50:
    print('Your grade is D')
else:
    print('Your grade is E')
