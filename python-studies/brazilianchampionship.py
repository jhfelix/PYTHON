import operator
seriea = ('Flamengo', 'Internacional','Atlético Mineiro','São Paulo',
    'Fluminense','Gremio','Palmeiras','Santos','Atletico-PR',
    'Bragantino','Ceara', 'Corinthians', 'Atletico-GO','Bahia',
    'Sport Recife', 'Fortaleza', 'Vasco', 'Goiás','Coritiba','Botafogo')
print( 'BRAZILIAN CHAMPIONSHIP 2020/2021 ')
print('''\nChoose one of the options below to display:
[A] The top 5
[B] The last 4 placed
[C] Times in alphabetical order
[D] What position is Sport Recife in?
[E]  Exit''')
while True:
    option = str(input('Enter the desired option: ')).upper().strip()
    if option == 'A':
        for c in (seriea[0:5]):
            print(c)
    elif option == 'B':
        print(seriea[-4:])
    elif option == 'C':
        print(sorted(seriea))
    elif option == 'D':
        #print('Sport is in {}o.'.format(seriea.index('Sport Recife')+1))
        print(f'Sport is in {seriea.index("Sport Recife")+1}ª. position')
    elif option == 'E':
        break
