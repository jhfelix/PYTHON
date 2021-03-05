print('-=-' *7, 'DELIBAB - DEBRECEN','-=-' *7 )

price = float(input('Enter purchase amount '))
print('''PAYMENT METHODS
    [1] cash payment
    [2] in sight card
    [3] 2 x on the card
    [4] 3 x or more quota on the card''')
op = int(input('Desired option '))
if op == 1:
    v1 = price - (price * 10 / 100)
    print(f'The value will be $  {v1:.2f}')
elif op == 2:
    v2 = price - (price * 5 / 100)
    print(f' The value will be $ {v2:.2f}')
elif op == 3:
    v3 = price
    p1 = v3 / 2
    print(f'The value will be $ {v3:.2f} and with quota $ {p1:.2f}')
elif op == 4:
    quota = int(input('In how many quota? '))
    v4 = price + (price * 20 / 100)
    p2 = v4 / quota
    print(f'The total amount will be $ {v4:.2f} and with quota R$ {p2:.2f}')
else:
    op = 0
    print('''
        \033[01;31mINVALID OPTION \033[m''')
print('''
Good shopping!''')

