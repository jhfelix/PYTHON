from datetime import date
current = date.today().year
birth = int(input('Enter the year of birth (YYYY) '))
gender = str(input('Type (F) -Female, (M) -Male: ').upper())
if gender == 'M':
    print('Another soldier')
else:
    print('You cannot enlist')
age = current - birth
print(f'Your age is {age}')
if age == 18 and gender == 'M':
    print('\033[01;32;43mYou have to enlist comrade \033[m')
elif age > 18 and gender == 'M':
    t = birth +18
    print(f'\033[03;33;47mIt is past your time to enlist, the year of your enlistment was in {t}. \033[m')
elif age < 18 and gender == 'M':
    print('Calm little grasshopper your time will come')



