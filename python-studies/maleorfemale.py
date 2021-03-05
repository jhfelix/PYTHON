gender = str(input('Enter your gender: [M / F] ')).strip().upper()[0]
while gender not in 'MmFf':
    gender = str(input('Invalid data, re-enter your gender')).strip().upper()[0]
print(f'Gender {gender} successfully registered ')
