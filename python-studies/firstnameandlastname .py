n = str (input ('Enter your full name ')). strip ()
name = n.split ()
print ('His first name is \033[1;30;46m {}\033[m'.format(name[0]))
print ('Your last name is {}'.format(name[len(name) -1]))