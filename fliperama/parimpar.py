# ==========================
# Arquivo: parimpar.py
# Disciplina: 2026-PCAP
# Aula: 18
# Autor: Gabriela
# Conceitos: funcao, operador %, repeticao e placar
# ==========================

from random import randint
from telas import titulo, linha
from modulos import ler_numero


def quem_venceu(soma, aposta):
    soma_par = soma % 2 == 0

    if soma_par and aposta == 'par':
        return 'jogador'

    if not soma_par and aposta == 'impar':
        return 'jogador'

    return 'computador'


def jogar_parimpar():
    titulo('JOGO PAR OU IMPAR')

    vitorias_jogador = 0
    vitorias_computador = 0

    for rodada in range(1, 6):
        print('Rodada ' + str(rodada) + ' de 5')

        numero_jogador = ler_numero('Escolha de 0 a 5', 0, 5)
        aposta = input('Digite par ou impar: ').strip().lower()

        while aposta not in ['par', 'impar']:
            print('Digite somente par ou impar.')
            aposta = input('Digite par ou impar: ').strip().lower()

        numero_computador = randint(0, 5)
        total = numero_jogador + numero_computador

        print('Computador escolheu ' + str(numero_computador) + '.')
        print('A soma foi ' + str(total) + '.')

        resultado = quem_venceu(total, aposta)

        if resultado == 'jogador':
            vitorias_jogador += 1
            print('Voce ganhou a rodada!')
        else:
            vitorias_computador += 1
            print('O computador ganhou a rodada!')

        print(
            'Placar: '
            + str(vitorias_jogador)
            + ' X '
            + str(vitorias_computador)
        )
        linha()

    if vitorias_jogador > vitorias_computador:
        titulo('VOCE VENCEU!')
    else:
        titulo('COMPUTADOR VENCEU!')
