# UDEMY
# Curso Python 3 | Aula 17
# Loop

repetir = 's'
fatura = list()
total = 0
validPreco = False

while repetir == 's':
    
    produto = str(input('\nDigite o produto: '))
    preco = input('Digite o valor: ')
    
    while validPreco == False:
        try:
            preco = float(preco)
            
            if preco <= 0:
                print('Digite um valor maior que zero.')
                preco = input('\nDigite o valor: ')
            else:
                validPreco = True
        except:
            print(f'Você digitou {preco}. Formato Inválido.')
            print(f'Use apenas Números e separe os centavos com "."')
            preco = input('\nDigite o valor: ')

    fatura.append([produto, preco])
    total += preco
    validPreco = False

    repetir = str(input('\nDeseja adicionar mais algum produto? [S/N] ')).lower()[0]

for item in fatura:
    print(f'{((item[0]).upper())} \t\tR$ {item[1]:.2f}')
    
print(f'O total desta fatura é R$ {total:.2f}')
    
print('-- Fim do Programa --')