phrase = str(input('Type a phrase ')).strip().upper()
words = phrase.split()
together = ''.join(words)
inverse = ''
for letter in range(len(together)-1, -1, -1):
    inverse += together[letter]
print(f'{together} {inverse}')
if inverse == together:
# inverse = together[::-1]
    print('Is a palindrome')
else:
    print('Not is a palindrome')
