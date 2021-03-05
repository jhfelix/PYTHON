import random
import time
pc = random.randint (0,5)
print ('-' * 20)
print ('Ill think of a number between 0 e 5 try it to guess')
print ('-' * 20)
player = int (input ('What number did I think of?'))
print ('Processing')
time.sleep (3)
if player == pc:
    print ('\033[01;33;45mYou won !!! \ 033 [m')
else:
    print ('\033[01;31;40mLOSER \ 033 [m')
print (pc)