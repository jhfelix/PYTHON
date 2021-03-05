from datetime import date
minor = 0
for c in range (1, 8):
    person = int (input (f'Enable the birth year of {c} ª person '))
    if date.today().year - person <21:
        minors += 1
print ('\n {} are Older and {} are Younger.'.format(7 - minor, minor))