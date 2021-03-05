greater = 0
less = 0
for c in range (1,6):
    weight = float (input (f'Insert the weight of {c} º person '))
    if c == 1:
        greater = weight
        less = weight
    else:
        if weight > greater:
            greater = weight
            if weight < less:
                less = weight
print (f'The biggest weight was {greater} kg ')
print (f'The smallest weight was {less} kg ')