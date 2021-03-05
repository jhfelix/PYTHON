tot = 0
num = int(input('Enter a number'))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[033m', end='')
        tot += 1
    else:
        print('\033[031m', end='')
    print(f'{c}', end='')
print(f'\n\033[mThe number of times that {num} and was divisible was {tot}')
if tot == 2:
    print('Its a prime number')
else:
    print('Not prime number')
