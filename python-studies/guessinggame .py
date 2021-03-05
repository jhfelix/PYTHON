from random import randint
from time import sleep
computer = randint (0,10)
print ('Im your computer ... I just thought of a number between 0 and 10')
sleep (3)
print ('Can you guess the number I thought?')
sleep (2)
hit = False
guess = 0
while not hit:
    player = int (input ('Whats your guess? '))
    guess += 1
    if player == computer:
        hit = True
    else:
        if player < computer:
            print ('More ... try again')
        elif player > computer:
            print ('Less ... try again')
print (f'Gone with {guess} attempts')