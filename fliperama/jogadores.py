# ====================================================================
# Arquivo: telas.py
# Disciplina: 2026-PCAP
# Aula: 22
# Autor: Gabriela
# Conceitos: registro como lista de campos, cadastro como lista de listas, cadastrar, listar, buscar, alterar, excluir, persistencia em arquivo .csv
# ====================================================================

# oque é este arquivo 
# a quarta gaveta d o projto, o telas.py cuida do que aparece, 
# o modulos.py cuida do que o programa pergunta,
#  o placar.py cuida de quantas partidas cada jogo teve, 
# e o jogadores.py cuida de quem jogou
#
# o registro
# cada jogador e uma lista de tres campos sempre nesta ordem
#  indice 0 -> apelido | 1 -> nome | 2 -> partidas
# e o cadastro e uma lista dessas listas
# ===================================================================

from telas import titulo, linha
from modulos import ler_opcao

def cadastrar(jogadores): 
    titulo('NOVO JOGADOR')

    apelido = input('Apelido (sem espaços): ').strip().lower()
    nome = input('Nome completo: ').strip()

    novo = [apelido, nome, '0']
    jogadores.append(novo)

    print('Jogador ' + apelido + ' cadastro.')
    linha()

def listar(jogadores):
    titulo('JOGADORES CADASTRADOS')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastrado ainda.')
    else:
        for jogador in jogadores:
            print(jogador[0] + ' | ' + jogador[1] + ' | ' + jogador[2] + ' partidas')


    linha()

def buscar(jogadores, apelido):
    for i in range(len(jogadores)):
        if jogadores[i][0] == apelido:
            return i

    return -1


def alterar(jogadores):
    listar(jogadores)

    apelido = input('Apelido de quem vai mudar de nome: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Nao achei ninguem com esse apelido.')
    else:
        print('Nome atual: ' + jogadores[i][1])
        jogadores[i][1] = input('nome novo: ').strip()
        print('pronto. agora e ' + jogadores[i][1] + '.')

linha()

def excluir(jogadores):
    listar(jogadores)

    apelido = input

jogadores = []

cadastrar(jogadores)
cadastrar(jogadores)
listar(jogadores)
print(jogadores)
