# ==========================
# Arquivo: modulos.py
# Disciplina: 2026-PCAP
# Aula: 23
# Autor: Gabriela
# Conceitos: validacao e reaproveitamento de funcoes
# ==========================


def ler_opcao(mensagem, validas):
    resposta = input(mensagem + ': ').strip()

    while resposta not in validas:
        print('Opcao invalida! Tente novamente.')
        resposta = input(mensagem + ': ').strip()

    return resposta


def ler_numero(mensagem, minimo, maximo):
    numeros_validos = []

    for numero in range(minimo, maximo + 1):
        numeros_validos.append(str(numero))

    resposta = ler_opcao(mensagem, numeros_validos)
    return int(resposta)


def ler_texto(mensagem):
    resposta = input(mensagem + ': ').strip()

    while resposta == '':
        print('Esse campo nao pode ficar vazio.')
        resposta = input(mensagem + ': ').strip()

    return resposta
