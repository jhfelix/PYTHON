list = ('zero', 'one', 'two', 'three', 'four',
     'five', 'six', 'seven', 'eight', 'nine',
     'ten' ,'eleven', 'twelve', 'thirteen', 'fourteen',
     'fifteen', 'sixteen', 'seventeen', 'eighteen',
     'nineteen', 'twenty')

while True:
    num = int (input ('Enter a number between 0 and 20: '))
    if num <0 or num> 20:
        print ('Invalid Try again', end = '')
    else:
        print (f'You entered the number {list [num]} ')
    resp = ''
    while resp not in 'SN':
        resp = str (input ('Do you want to continue? Y / N')).upper().strip() [0]
    if resp == 'N':
        break
print ("PROGRAM FINISHED")