import matplotlib.pyplot as plt
import time

def titulo(texto):
    ciano = '\033[36m'
    fecha = '\033[m'
    tamanho = len(texto) + 10
    
    print('\n' + (f'{ciano}~{fecha}' * tamanho))
    print((f'{texto:^{tamanho}}').upper())
    print((f'{ciano}~{fecha}' * tamanho) + '\n')

def validaNumeros (mensagem):

    """
    VALIDADOR DE NÚMEROS

    Verifica se o valor do input é uma string ou um número e apresenta uma mensagem de atenção ou erro caso necessário.

    """
    
    valida = False

    while valida == False:
        numero = input(mensagem)
        try:
            numero = int(numero)
            if numero <= 1:
                mensagemAtenção()
            else:
                return numero
                valida = True                
        except:
            mensagemErro()

def mensagemAtenção():

    """
    MENSAGEM DE ATENÇÃO

    Exibe uma mensagem de atenção, separada por categoria, texto e destaque (exemplo).

    """

    cores = ('\033[33m', '\033[m')
    
    atençãoCategoria = f'{cores[0]}[ATENÇÃO]{cores[1]} '
    atençãoMensagem = f'Insira um número maior do que '
    atençãoExemplo = f'{cores[0]}"1"{cores[1]}'

    
    atenção = atençãoCategoria + atençãoMensagem + atençãoExemplo + '.'

    print(f'{cores[0]}-{cores[1]}' * (len(atenção) - 16))
    print(atenção)
    print(f'{cores[0]}-{cores[1]}' * (len(atenção) - 16) + '\n')

def mensagemComeçar():

    cores = ('\033[32m', '\033[m')
    
    começarMensagem = 'Assim que apertar a tecla [enter], você deverá escrever o seu nome o mais rápido possível.'
    
    print(f'{cores[0]}-{cores[1]}' * len(começarMensagem))
    print(começarMensagem)
    print(f'{cores[0]}-{cores[1]}' * len(começarMensagem))

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

vezes = list()
tempo = list()
legenda = list()

titulo('Teste de Velocidade')

print('Quantas repetições você quer?')
tentativas = validaNumeros('Repetições: ')

print()
mensagemComeçar()
input()

for x in range (1, tentativas + 1):
    inicio = time.perf_counter()
    input(f'\nTentativa {x}: ')
    fim = time.perf_counter()
    tempo.append(round(fim - inicio, 2))
    vezes.append(x)
    legenda.append(f'Tentativa {x}')

plt.xticks(vezes, legenda)
plt.plot(vezes, tempo)
plt.show()
