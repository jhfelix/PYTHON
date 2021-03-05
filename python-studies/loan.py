house = float(input('Enter the value of the house '))
salary = float(input('Enter your salary '))
years = int(input('Enter the number of years '))
installment = house / (years * 12)
minimum = salary * 30/100
print('The installment will be: {:.2f}'.format(installment))
if installment <= minimum:
    print('Loan granted')
else:
    print('Loan not granted')