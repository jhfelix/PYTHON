print ('-' * 23)
print ('Analyzing triangles')
print ('-' * 23)
a = float (input ("Enter the first segment" ))
b = float (input ("Enter the second segment" ))
c = float (input ("Enter the third segment" ))
if a <b + c and b <a + c and c <a + b:
    print ('Form triangle')
else:
    print ('Not triangular shape')