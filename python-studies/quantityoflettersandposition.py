phrase = str (input ('Enter a phrase ')). strip (). upper ()
print ('The amount of A that appears is {}'. format (phrase.count ('A')))
print ('The position that appears the first time {}'. format (phrase.find ('A') + 1))
print ('The position that appears last {}'. format (phrase.rfind ('A') + 1))