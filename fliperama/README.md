# Fliperama do ASH

Projeto de terminal organizado por Gabriela para a disciplina PCAP. O programa
possui quatro jogos, placar salvo e uma área para cadastrar jogadores.

## O que o programa faz

- Abre os jogos Adivinhe o Número, Pedra-Papel-Tesoura e Par ou Ímpar;
- Acrescenta o jogo autoral Quiz de Informática;
- Conta quantas vezes cada jogo foi aberto;
- Cadastra, lista, altera e exclui jogadores;
- Mostra um ranking com os dez jogadores que mais participaram;
- Salva o placar e o cadastro em arquivos CSV.

## Como executar

```bash
cd fliperama
python3 main.py
```

## Arquivos do projeto

- `main.py`: apresenta o menu e chama cada parte do programa;
- `telas.py`: desenha títulos e linhas;
- `modulos.py`: reúne as funções que validam as respostas;
- `placar.py`: lê e salva as contagens dos jogos;
- `jogadores.py`: possui cadastro, busca, ranking, alteração e exclusão;
- `adivinhe.py`, `ppt.py`, `parimpar.py` e `meujogo.py`: arquivos dos jogos;
- `placar.csv` e `jogadores.csv`: dados salvos;
- `README-meujogo.md`: explicação do Quiz de Informática.

A função `ler_texto()` está no `modulos.py` porque ela pode ser usada por
qualquer parte que precise validar um texto. Com isso, o `jogadores.py` não
precisa repetir o mesmo laço de validação em várias funções.

## Como o projeto foi construído

- Aula 20: os jogos foram separados em módulos e colocados no menu;
- Aula 21: o placar começou a ser salvo em arquivo;
- Aula 22: foi criado o cadastro com as operações de incluir, ler, alterar e
  excluir;
- Aula 23: campos vazios foram bloqueados e a documentação foi finalizada.

## Exemplo de execução

```text
============================================
              FLIPERAMA DO ASH
============================================
1 - Jogo Adivinhe o Numero
2 - Jogo Pedra, Papel e Tesoura
3 - Jogo Par ou Impar
4 - Quiz de Informatica
5 - Cadastro de Jogadores
0 - Sair do Fliperama
============================================
Escolha uma opcao: 4
Quem vai jogar? Digite o apelido: gabi
```

## O que ainda não funciona

- Nomes com vírgula não podem ser usados, pois a vírgula separa os campos do
  arquivo CSV;
- O Quiz de Informática ainda tem somente três perguntas fixas.

## Autoavaliação

Conceito que eu acredito que o trabalho vale: **B**

### Mapa do projeto

| Parte | Arquivo | Função principal |
|---|---|---|
| Adivinhe o Número | `adivinhe.py` | `jogar_adivinhe` |
| Pedra-Papel-Tesoura | `ppt.py` | `jogar_ppt` |
| Par ou Ímpar | `parimpar.py` | `jogar_parimpar` |
| Quiz de Informática | `meujogo.py` | `jogar_meujogo` |
| Cadastro | `jogadores.py` | `menu_jogadores` |
| Ranking | `jogadores.py` | `listar` |
| Arquivos do placar | `placar.py` | `carregar_placar` e `salvar_placar` |

### Critérios e provas

| Critério | Nível | Prova no projeto |
|---|---|---|
| 1. Estrutura e registro | B | cabeçalho e oito docstrings em `jogadores.py` |
| 2. Operações do cadastro | B | funções `cadastrar`, `listar`, `alterar` e `excluir` |
| 3. Busca e índice | B | função `buscar` e verificação de `-1` |
| 4. Persistência | B | funções de salvar e carregar dos arquivos CSV |
| 5. Documentação | B | os dois arquivos README e este exemplo de execução |
| 6. Jogo autoral | B | Quiz em `meujogo.py` e opção 4 do `main.py` |

### Uso de IA

Usei o ChatGPT para ajudar a conferir os requisitos, organizar os arquivos e
testar o programa. Revisei o código para entender o menu, as validações, o
cadastro e as regras dos jogos.
