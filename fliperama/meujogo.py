# ==========================
# Arquivo: meujogo.py
# Disciplina: 2026-PCAP
# Aula: 23
# Autor: Gabriela
# Conceitos: lista de listas, repeticao, validacao e pontuacao
# ==========================

from telas import titulo, linha
from modulos import ler_opcao


PERGUNTAS = [
    [
        'Qual componente executa as instrucoes do computador?',
        'Teclado',
        'Processador',
        'Monitor',
        '2'
    ],
    [
        'Qual e a extensao de um arquivo Python?',
        '.jpg',
        '.py',
        '.mp3',
        '2'
    ],
    [
        'Qual comando mostra uma mensagem na tela?',
        'print',
        'input',
        'randint',
        '1'
    ]
]


def jogar_meujogo():
    '''Aplica um quiz de tres perguntas e vence quem acerta duas ou mais.'''
    titulo('QUIZ DE INFORMATICA')

    acertos = 0

    for indice in range(len(PERGUNTAS)):
        pergunta = PERGUNTAS[indice]

        print('Pergunta ' + str(indice + 1) + ' de 3')
        print(pergunta[0])
        print('[1] ' + pergunta[1])
        print('[2] ' + pergunta[2])
        print('[3] ' + pergunta[3])

        resposta = ler_opcao('Resposta', ['1', '2', '3'])

        if resposta == pergunta[4]:
            acertos += 1
            print('Resposta correta!')
        else:
            print('Resposta incorreta. A certa era: ' + pergunta[int(pergunta[4])])

        linha()

    print('Total de acertos: ' + str(acertos) + ' de 3.')

    if acertos >= 2:
        titulo('VOCE VENCEU O QUIZ!')
    else:
        titulo('TENTE OUTRA VEZ!')
