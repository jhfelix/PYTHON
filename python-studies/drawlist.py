import random
n1 = str (input ('Name 1'))
n2 = str (input ('Name 2'))
n3 = str (input ('Name 3'))
n4 = str (input ('Name 4'))
list = [n1, n2, n3, n4]
chosen = random.shuffle (list)
print ('The order is {}')
print (list)