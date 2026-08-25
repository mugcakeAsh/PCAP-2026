# ==========================
# Arquivo: main.py
# Disciplina: 2026-PCAP
# Aula: 20
# Autor: Gabriela
# Data: 2026.08.04
# Conceitos:
# ==========================

from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar

NOME_DOS_JOGOS = ['Adivinhe o numero', 'Pedra-papel-tesoura', 'Par ou Impar']
vezes_jogados = carregar_placar()

def mostrar_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOME_DOS_JOGOS[i] + ': ' + str(vezes_jogados[i]) + 'x')

NOME_DO_DONO = 'ASH'
OPCOES = ['0', '1', '2']

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo adivinhe o número')
    print('2 - Jogo pedra, papel e tesoura')
    print('0 - Sair do Fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogados)
        titulo('Até a próxima!')
        break
   
    indice = int(opcao) - 1
    vezes_jogados[indice] = vezes_jogados[indice] + 1

    if opcao == '1':
        jogar_adivinhe()
    elif opcao == '2':
        jogar_ppt()