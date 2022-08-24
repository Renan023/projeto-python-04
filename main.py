import datetime
y, m, d = 2022,8 ,23
at ,dat = datetime.date.today().year, datetime.date.today()
print(dat)
ma, me = 0, 0
r = 'S'
while r=='S':
    print('='*30)
    n = input('Nome: ')
    nasc = int(input('Nascimento: '))
    id = at- nasc
    print('Idade: {} anos'.format(id))
    c = input('Cidade: ')
    b = input('Bairro: ')
    if id>=18:
        print('{} é de maior '.format(n))
        print('Dirija-se a sala 01')
        ma += 1
    else:
        print('{} é de menor '.format(n))
        print('Dirija-se a sala 02')
        me += 1
    r = input('Continuar? [S/N] ').upper()
    print('='*30)
print('Foram cadastrados neste período {} maior e {} menor'.format(ma,me))
