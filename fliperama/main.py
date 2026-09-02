# ==========================
# Arquivo: main.py
# Disciplina: 2026-PCAP
# Aula: 23
# Autor: Gabriela
# Data: 2026.09.02
# Conceitos: modulos, menu, listas, cadastro e persistencia
# ==========================

from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_parimpar
from meujogo import jogar_meujogo
from modulos import ler_opcao, ler_texto
from placar import salvar_placar, carregar_placar
from jogadores import (
    buscar,
    carregar_jogadores,
    menu_jogadores,
    salvar_jogadores
)


NOME_DO_DONO = 'ASH'

OPCOES = ['0', '1', '2', '3', '4', '5']

NOME_DOS_JOGOS = [
    'Adivinhe o numero',
    'Pedra-papel-tesoura',
    'Par ou Impar',
    'Quiz de Informatica'
]

vezes_jogados = carregar_placar()
cadastro = carregar_jogadores()


def mostrar_menu():
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o Numero')
    print('2 - Jogo Pedra, Papel e Tesoura')
    print('3 - Jogo Par ou Impar')
    print('4 - Quiz de Informatica')
    print('5 - Cadastro de Jogadores')
    print('0 - Sair do Fliperama')
    linha()


def mostrar_placar():
    titulo('PLACAR DO FLIPERAMA')

    for indice in range(len(vezes_jogados)):
        print(
            NOME_DOS_JOGOS[indice]
            + ': '
            + str(vezes_jogados[indice])
            + 'x'
        )

    linha()


while True:
    mostrar_menu()
    opcao = ler_opcao('Escolha uma opcao', OPCOES)

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogados)
        salvar_jogadores(cadastro)
        titulo('ATE A PROXIMA!')
        break

    if opcao == '5':
        menu_jogadores(cadastro)
    else:
        posicao_jogo = int(opcao) - 1
        vezes_jogados[posicao_jogo] += 1

        apelido = ler_texto('Quem vai jogar? Digite o apelido').lower()
        posicao_jogador = buscar(cadastro, apelido)

        if posicao_jogador != -1:
            partidas = int(cadastro[posicao_jogador][2]) + 1
            cadastro[posicao_jogador][2] = str(partidas)
        else:
            print('Apelido nao cadastrado. O jogo abrira sem contar na ficha.')

        if opcao == '1':
            jogar_adivinhe()
        elif opcao == '2':
            jogar_ppt()
        elif opcao == '3':
            jogar_parimpar()
        else:
            jogar_meujogo()

        input('Pressione Enter para voltar ao menu... ')
