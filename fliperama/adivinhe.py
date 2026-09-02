# ==========================
# Arquivo: adivinhe.py
# Disciplina: 2026-PCAP
# Aula: 20
# Autor: Gabriela
# Data: 2026.08.04
# Conceitos: repeticao, condicao, sorteio e contador
# ==========================

from random import randint
from telas import titulo, linha
from modulos import ler_numero


def jogar_adivinhe():
    titulo('JOGO ADIVINHE O NUMERO')
    print('Tente adivinhar o numero que estou pensando entre 1 e 10.')

    segredo = randint(1, 10)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = ler_numero('Digite seu palpite', 1, 10)
        tentativas += 1

        if palpite < segredo:
            print('O numero secreto e maior. Tente novamente.')
        elif palpite > segredo:
            print('O numero secreto e menor. Tente novamente.')
        else:
            acertou = True
            print(
                'Parabens! Voce acertou o numero '
                + str(segredo)
                + ' em '
                + str(tentativas)
                + ' tentativa(s).'
            )

    linha()
