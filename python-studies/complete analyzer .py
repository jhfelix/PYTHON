
sumage = 0
majorityofman = 0
mediaage = 0
nameolder = ''
totwoman = 0
for c in range(1,5):
    print(f'---------- {c}ª Person ----------')
    name = str(input('Name: '))
    age = int(input('Age: '))
    gender = str(input('M/F: ')).strip()
    sumage += age
    if c == 1 and gender in 'Mm':
        majorityofman = age
        nameolder = name
    if gender in 'Mm' and age > majorityofman:
        majorityofman = age
        nameolder = name
    if gender in 'Ff' and age < 20:
        totwoman +=1
mediaage = sumage / 4
print(f'The average of the group: {mediaage}')
print(f'The oldest man is the age of {majorityofman} and its called {nameolder}')
print(f'The total number of women under 20: {totwoman}')

