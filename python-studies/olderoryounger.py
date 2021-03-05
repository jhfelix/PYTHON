from datetime import date
current = date.today (). year
totolder = 0
totyounger = 0
for people in range (1,8):
    birth = int (input ('What year were you born in? '))
    age = current - birth
    if age >= 18:
        totolder += 1
    else:
        totyounger += 1
print (f'Ao altogether we had {totolder} of older ')
print (f'Ao altogether we had {totyounger} of minor')