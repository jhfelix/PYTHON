from random import randint
import time
items = ('stone', 'paper', 'scissors')
computer = randint (0, 2)
print ('''YOUR OPTIONS ARE:
[0] STONE
[1] PAPER
[2] SCISSORS ''')
player = int (input ('Whats your move? '))
print ('JO')
time.sleep (1)
print ('KEN')
time.sleep (1)
print ('PO ...')
time.sleep (1)
print (f'The computer played {items [computer]} ')
print (f'The player played {items [player]} ')

if computer == 0:
    if player == 0:
        print ('TIE')
    elif player == 1:
        print ('PLAYER WON')
    elif player == 2:
        print ('COMPUTER WON')
    else:
        print ('INVALID PLAY')
elif computer == 1:
    if player == 0:
        print ('COMPUTER WON')
    elif player == 1:
        print ('TIE')
    elif player == 2:
        print ('PLAYER WON')
    else:
        print ('INVALID PLAY')
elif computer == 2:
    if player == 0:
        print ('PLAYER WON')
    elif player == 1:
        print ('COMPUTER WON')
    elif player == 2:
        print ('TIE')
    else:
        print ('INVALID PLAY')