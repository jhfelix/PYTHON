s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        s+=c
print(cont,s)

'''
cont = 0
s = 0
for c in range (1, 7):
    num = int (input ('Enter a number'))
    if num% 2 == 0:
        s += num
        cont += 1
print (f'The sum of the numbers = {s} and {cont} were evaluated ')
'''