# ==========================
# Arquivo: placar.py
# Disciplina: 2026-PCAP
# Aula: 21
# Autor: Gabriela
# Conceitos: leitura e gravacao de arquivo CSV
# ==========================

from os.path import exists


ARQUIVO = 'placar.csv'

NOMES = [
    'Adivinhe o numero',
    'Pedra-papel-tesoura',
    'Par ou Impar',
    'Quiz de Informatica'
]


def salvar_placar(vezes):
    arquivo = open(ARQUIVO, 'w')

    for indice in range(len(vezes)):
        arquivo.write(NOMES[indice] + ',' + str(vezes[indice]) + '\n')

    arquivo.close()


def carregar_placar():
    if not exists(ARQUIVO):
        return [0, 0, 0, 0]

    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    contagens = []

    for linha_lida in linhas:
        pedacos = linha_lida.strip().split(',')

        if len(pedacos) == 2:
            contagens.append(int(pedacos[1]))

    while len(contagens) < len(NOMES):
        contagens.append(0)

    return contagens[:len(NOMES)]
