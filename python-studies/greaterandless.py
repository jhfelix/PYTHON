lst = []
for c in range(1, 6):
    weight = float(input(f'weight of {c} ª person: '))
    lst += [weight]
print('')
print('The biggest weight was:', max(lst))  # maximum value in the list
print("The smallest weight was:", min(lst))  # minimal value in the list
