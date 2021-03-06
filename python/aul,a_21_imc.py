from time import sleep


def titulo(texto):
    ciano = '\033[36m'
    fecha = '\033[m'
    tamanho = len(texto) + 10
    
    print('\n' + (f'{ciano}~{fecha}' * tamanho))
    print((f'{texto:^{tamanho}}').upper())
    print((f'{ciano}~{fecha}' * tamanho) + '\n')

def mensagemAtenção():

    """
    MENSAGEM DE ATENÇÃO

    Exibe uma mensagem de atenção, separada por categoria, texto e destaque (exemplo).

    """

    cores = ('\033[33m', '\033[m')
    
    atençãoCategoria = f'{cores[0]}[ATENÇÃO]{cores[1]} '
    atençãoMensagem = f'Insira um número acima de '
    atençãoExemplo = f'{cores[0]}"0"{cores[1]}'

    
    atenção = atençãoCategoria + atençãoMensagem + atençãoExemplo + '.'

    print(f'{cores[0]}-{cores[1]}' * (len(atenção) - 16))
    print(atenção)
    print(f'{cores[0]}-{cores[1]}' * (len(atenção) - 16) + '\n')

def mensagemErro():

    """
    MENSAGEM DE ERRO

    Exibe uma mensagem de erro, separada por categoria, texto e destaque (exemplo).

    """

    cores = ('\033[31m', '\033[m')
    erroMensagem = f'Insira apenas '
    erroExemplo = f'{cores[0]}NÚMEROS{cores[1]}'
    erroCategoria = f'{cores[0]}[ERRO]{cores[1]} '
    
    erro = erroCategoria + erroMensagem + erroExemplo + '.'

    print(f'{cores[0]}-{cores[1]}' * (len(erro) - 16))
    print(erro)
    print(f'{cores[0]}-{cores[1]}' * (len(erro) - 16) + '\n')

def validaNumeros (mensagem):

    """
    VALIDADOR DE NÚMEROS

    Verifica se o valor do input é uma string ou um número e apresenta uma mensagem de atenção ou erro caso necessário.

    """
    
    valida = False

    while valida == False:
        numero = input(mensagem)
        try:
            numero = float(numero)
            if numero <= 0:
                mensagemAtenção()
            else:
                return numero
                valida = True                
        except:
            mensagemErro()

def imc(peso, altura):

    """
    CÁLCULO IMC

    Calcula e retorna o IMC a partir do peso e da altura.
    
    """

    calculoImc = peso / altura ** 2
    return calculoImc

def classificIMC (imc):
    
    """
    CALSSIFICAÇÃO DO IMC

    Apresenta a classificação baseada no IMC

    """
    verde = '\033[32m'
    amarelo = '\033[33m'
    vermelho = '\033[31m'
    underline = '\033[4m'
    fecha = '\033[m'

    if imc >= 40:
        print(f'\n{vermelho}•{fecha} Com o peso {underline}{peso}kg{fecha} e a altura {underline}{altura}{fecha}, sua classificação é: {vermelho}OBESIDADE MÓRBIDA{fecha}\n')
    elif imc >= 35:
        print(f'\n{vermelho}•{fecha} Com o peso {underline}{peso}kg{fecha} e a altura {underline}{altura}{fecha}, sua classificação é: {vermelho}OBESIDADE GRAU II{fecha}\n')    
    elif imc >= 30:
        print(f'\n{amarelo}•{fecha} Com o peso {underline}{peso}kg{fecha} e a altura {underline}{altura}{fecha}, sua classificação é: {amarelo}OBESIDADE GRAU I{fecha}\n')    
    elif imc >= 25:
        print(f'\n{amarelo}•{fecha} Com o peso {underline}{peso}kg{fecha} e a altura {underline}{altura}{fecha}, sua classificação é: {amarelo}SOBREPESO{fecha}\n')    
    elif imc >= 18.5:
        print(f'\n{verde}•{fecha} Com o peso {underline}{peso}kg{fecha} e a altura {underline}{altura}{fecha}, sua classificação é: {verde}PESO NORMAL{fecha}\n') 
    else:
        print(f'\n{amarelo}•{fecha} Com o peso {underline}{peso}kg{fecha} e a altura {underline}{altura}{fecha}, sua classificação é: {amarelo}ABAIXO DO PESO{fecha}\n')



# Programa Principal
# .................................

titulo('CALCULADORA DE IMC')

sleep(0.5)

peso = validaNumeros('• Digite seu Peso: ')
altura = validaNumeros('• Digite sua Altura: ')

sleep(0.3)
print()
print('Calculando seu IMC ...')
sleep(1.0)

classificIMC(imc(peso, altura))