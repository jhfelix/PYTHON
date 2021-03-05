password = '54321'
reading = ''
while (reading != password):
    reading = (input ('Enter a password'))
    if reading == password:
        print ('Access cleared')
    else:
        print ('Incorrect password, try again')