# ============================================================
# ARQUIVO   : ppt.py (pasta fliperama)
# Conceitos : jogo como modulo, lista, funcao com retorno e %
# Base      : jogo da Aula 17
# Autor     : Gabriela
# Data      : 11.08.2026
# ============================================================

from random import randint
from telas import titulo, linha
from modulos import ler_opcao


JOGADAS = ['PEDRA', 'PAPEL', 'TESOURA']


def quem_vence(jogador, computador):
    if jogador == computador:
        return 'empate'

    if jogador == (computador + 1) % 3:
        return 'jogador'

    return 'computador'


def mostrar_jogadas():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')
    linha()


def jogar_ppt():
    titulo('PEDRA - PAPEL - TESOURA')

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao('Sua jogada', ['0', '1', '2']))
        computador = randint(0, 2)

        print('Voce jogou ' + JOGADAS[jogador] + '.')
        print('Computador jogou ' + JOGADAS[computador] + '.')

        resultado = quem_vence(jogador, computador)

        if resultado == 'empate':
            print('Empate! Ninguem pontuou.')
        elif resultado == 'jogador':
            pontos_jogador += 1
            print('Voce venceu essa rodada!')
        else:
            pontos_computador += 1
            print('Computador venceu essa rodada!')

        linha()
        print(
            'Placar: Jogador '
            + str(pontos_jogador)
            + ' X '
            + str(pontos_computador)
            + ' Computador'
        )
        linha()

    if pontos_jogador > pontos_computador:
        titulo('YOU WIN!')
    else:
        titulo('YOU LOSE!')
