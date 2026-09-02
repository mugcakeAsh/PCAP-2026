# ====================================================================
# Arquivo    : jogadores.py (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 22 - cadastro de jogadores
# Autor      : Gabriela
# Revisado   : Aula 23 - campos vazios e documentacao
# Conceitos  : registro, lista de listas, CRUD, busca e arquivo CSV
# ====================================================================

from os.path import exists
from telas import titulo, linha
from modulos import ler_opcao, ler_texto


ARQUIVO = 'jogadores.csv'


def cadastrar(jogadores):
    '''
    Recebe apelido e nome e coloca uma ficha nova na lista.

    A lista recebida e alterada, por isso a funcao nao precisa devolver nada.
    '''
    titulo('CADASTRAR JOGADOR')

    apelido = ler_texto('Apelido sem espacos').lower()
    posicao = buscar(jogadores, apelido)

    if posicao != -1:
        print('Esse apelido ja pertence a outro jogador.')
        linha()
        return

    nome = ler_texto('Nome completo')
    ficha = [apelido, nome, '0']
    jogadores.append(ficha)

    print(apelido + ' foi cadastrado com sucesso.')
    linha()


def listar(jogadores):
    '''Mostra no maximo dez jogadores, começando por quem mais jogou.'''
    titulo('RANKING DOS JOGADORES')

    if len(jogadores) == 0:
        print('Ainda nao existe nenhum jogador cadastrado.')
    else:
        top_dez = sorted(
            jogadores,
            key=lambda ficha: int(ficha[2]),
            reverse=True
        )[:10]

        for lugar in range(len(top_dez)):
            jogador = top_dez[lugar]
            print(
                str(lugar + 1)
                + ' - '
                + jogador[0]
                + ' | '
                + jogador[1]
                + ' | '
                + jogador[2]
                + ' partida(s)'
            )

    linha()


def buscar(jogadores, apelido):
    '''
    Procura o apelido dentro da lista de jogadores.

    Recebe o cadastro e o apelido em letras minusculas. Devolve a posicao da
    ficha encontrada ou -1 quando o apelido nao existe.
    '''
    for posicao in range(len(jogadores)):
        if jogadores[posicao][0] == apelido:
            return posicao

    return -1


def alterar(jogadores):
    '''Procura um jogador pelo apelido e troca apenas o nome completo.'''
    listar(jogadores)

    apelido = ler_texto('Apelido de quem tera o nome alterado').lower()
    posicao = buscar(jogadores, apelido)

    if posicao == -1:
        print('Esse apelido nao foi encontrado.')
    else:
        print('Nome atual: ' + jogadores[posicao][1])
        novo_nome = ler_texto('Digite o nome novo')
        jogadores[posicao][1] = novo_nome
        print('O nome foi alterado para ' + novo_nome + '.')

    linha()


def excluir(jogadores):
    '''
    Exclui uma ficha somente depois de localizar e confirmar a escolha.
    '''
    listar(jogadores)

    apelido = ler_texto('Apelido que sera excluido').lower()
    posicao = buscar(jogadores, apelido)

    if posicao == -1:
        print('Esse apelido nao foi encontrado.')
    else:
        print('Jogador encontrado: ' + jogadores[posicao][1])
        print('[1] Confirmar exclusao')
        print('[2] Cancelar')
        confirmar = ler_opcao('Escolha', ['1', '2'])

        if confirmar == '1':
            jogadores.pop(posicao)
            print('Jogador excluido.')
        else:
            print('A exclusao foi cancelada.')

    linha()


def salvar_jogadores(jogadores):
    '''Escreve uma linha no CSV para cada ficha do cadastro.'''
    arquivo = open(ARQUIVO, 'w')

    for ficha in jogadores:
        arquivo.write(ficha[0] + ',' + ficha[1] + ',' + ficha[2] + '\n')

    arquivo.close()


def carregar_jogadores():
    '''Carrega o CSV ou cria um cadastro vazio quando o arquivo nao existe.'''
    if not exists(ARQUIVO):
        return []

    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    jogadores = []

    for linha_lida in linhas:
        campos = linha_lida.strip().split(',')

        if len(campos) == 3:
            jogadores.append(campos)

    return jogadores


def menu_jogadores(jogadores):
    '''Mostra o menu e chama as quatro operacoes do cadastro.'''
    while True:
        titulo('AREA DOS JOGADORES')
        print('[1] Cadastrar')
        print('[2] Ver ranking')
        print('[3] Alterar nome')
        print('[4] Excluir cadastro')
        print('[0] Voltar ao Fliperama')
        linha()

        escolha = ler_opcao('Escolha', ['0', '1', '2', '3', '4'])

        if escolha == '0':
            break
        elif escolha == '1':
            cadastrar(jogadores)
        elif escolha == '2':
            listar(jogadores)
        elif escolha == '3':
            alterar(jogadores)
        else:
            excluir(jogadores)
