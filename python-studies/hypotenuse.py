from math import hypot
co = float (input ('Opposite leg length?'))
ca = float (input ('Adjacent leg length?'))
hy = hypot (co, ca)
print (f'The hypotenuse is: {hy: .2f} ')

'''
import math
a = float (input ('What is the angle?'))
c = math.cos (math.radians (a))
s = math.sin (math.radians (a))
t = math.tan (math.radians (a))
print ('The cosine is? {: .2f}, The sine is? {:.2f}, The tangent is? {:.2f}'.format (c,s,t))

'''