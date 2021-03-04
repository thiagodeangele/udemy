# UDEMY
# Curso Python 3 | Aula 19
# Controle de notas/faltas de um aluno com tratamento de erros


# Validando Nome ................

validador = False

while validador == False:
    nome = input('\nDigite o nome do aluno: ').strip()
    if nome.isnumeric():
        print('Apenas textos')
    else:
        nome = str(nome)
        validador = True

# Validando Nota 1 ................

validador = False

while validador == False:
    nota1 = input('\n1ª Nota: ')
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print('\n[ERRO] Nota inválida. 0 - 10')
        else:
            validador = True
    except:
        print('\n[ERRO] Nota Inválida')


# Validando Nota 2 ................

validador = False

while validador == False:
    nota2 = input('\n2ª Nota: ')
    try:
        nota2 = float(nota2)
        if nota2 < 0 or nota2 > 10:
            print('\n[ERRO] Nota inválida. 0 - 10')
        else:
            validador = True
    except:
        print('\n[ERRO] Nota Inválida')


# Validando Faltas  ................

validador = False

while validador == False:
    faltas = input('\nFaltas: ')
    try:
        faltas = int(faltas)
        if faltas < 1 or faltas > 20:
            print('\n[ERRO] Digite um valor entre 1 e 20')
        else:
            validador = True
    except:
        print('\n[ERRO] Somente Números')




media = (nota1 + nota2)/2
frequencia = (20 - faltas)/20

if frequencia >= 0.7:
    if media >= 6:
        print('Aprovado')
    elif media < 6:
        print('Reprovado por Média')    
elif frequencia < 0.7:
    print('Reprovado por Faltas')
else:
    print('Erro')
