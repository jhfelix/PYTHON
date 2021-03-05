num = int(input('Enter a number '))
print('''Choose the option:
      [1] Convert to binary
      [2] Convert to octal
      [3] Convert to Hex ''')
op = int(input('Your option'))
if op == 1:
    print('The number will be {}'.format((bin(num))))
elif op == 2:
    print('The number will be {}'.format(oct(num)))
elif op == 3:
    print('The number will be {}'.format(hex(num)))
else:
    print('Invalid number')
