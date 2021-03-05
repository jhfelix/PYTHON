import datetime
year = int(input('Enter the year you want to analyze, if you want to analyze the current year, type 0: '))
if year == 0:
    year = datetime.date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'Year is leap {year}')
else:
    print(f'Year is not a leap year {year}')
