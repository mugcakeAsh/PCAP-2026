# Fliperama da Gabriela

MeuApp v3.0 — aulas 28 e 29 de PCAP.

## O que faz

O programa tem cadastro de jogadores e o jogo Adivinhe o Número.
Dá para ver os jogadores e quantas partidas cada um jogou.
Só pode jogar com um apelido cadastrado. O cadastro aceita até 50 pessoas.

## Como rodar

Na raiz do repositório:

```bash
cd fliperama-c
gcc -Wall fliperama.c -o fliperama
./fliperama
```

Escolha 1 para jogar, 2 para cadastrar, 3 para listar ou 0 para salvar e sair.
O apelido deve ter até 19 caracteres, sem espaços nem vírgulas.
O programa diferencia letras maiúsculas e minúsculas.
É preciso rodar dentro da pasta `fliperama-c` para ler o CSV certo.
Se o arquivo não existir, a lista começa vazia. As mudanças são salvas pelo 0.

## Arquivos

- `fliperama.c`: programa em C.
- `jogadores.csv`: apelido e partidas de cada jogador.
- `README.md`: explicação da atividade.

Os jogadores cadastrados pelo menu são wesley, gustavo e italo.
O executável fica fora do Git pelo `.gitignore`, linhas 3 e 4.
O arquivo de jogadores do Python é separado deste.

## Python × C

As linhas do Python são de `fliperama/jogadores.py`.
As linhas do C são de `fliperama-c/fliperama.c`.

| Operação | Python | C | Explicação |
|---|---|---|---|
| Colocar um jogador na lista | Linha 37: `jogadores.append(ficha)` | Linhas 90–93: `strcpy`, partidas em 0 e `return qtd + 1` | No C, o apelido é copiado para o vetor e a quantidade aumenta. |
| Ver se o apelido é igual | Linha 80: `jogadores[posicao][0] == apelido` | Linha 63: `strcmp(apelidos[i], procurado) == 0` | O `strcmp` compara as letras dos dois apelidos. |
| Abrir o arquivo para salvar | Linha 132: `open(ARQUIVO, 'w')` | Linha 138: `fopen(ARQUIVO, "w")` | O C usa `FILE *` para trabalhar com o arquivo. |

## O que o C me obrigou a decidir

A linha 16 de `fliperama.c` define que cabem 50 jogadores.
Como esse espaço é fixo, a linha 74 confere se ainda cabe alguém antes de cadastrar.

No teste com capacidade 2, a terceira tentativa foi recusada.
O arquivo final está com capacidade 50.

## Autoavaliação

Conceito esperado: C.

| Critério | Conceito | Onde está |
|---|---|---|
| 1. Estrutura e Git | C | `fliperama.c`, linhas 1–18: cabeçalho, nome e constantes. Compila sem avisos com `-Wall`. `.gitignore`, linhas 3–4: executáveis ignorados. O histórico registra as etapas. |
| 2. Cadastro | C | `fliperama.c`, linha 32: validação. Linhas 59–106: busca, cadastro e lista. Linha 74: limite. Linha 85: apelido repetido. |
| 3. Jogo | C | `fliperama.c`, linhas 108–135: confere quem vai jogar, soma a partida e pede palpites de 1 a 100. |
| 4. Arquivo | C | `fliperama.c`, linhas 137–165: salvar e carregar. Linha 185: carrega ao abrir. Linha 201: salva ao sair. `jogadores.csv`, linhas 1–3: três jogadores. |
| 5. README | C | Este arquivo tem seis seções, a tabela com as três operações e a explicação do limite do vetor. |

Os testes conferiram opções inválidas, apelido repetido, cadastro cheio,
partida do jogador certo e a abertura sem CSV. Também foi conferido se os
jogadores e a partida voltam depois de fechar.

Exercício-minuto: a frase C vale nas duas versões. Quando não tem arquivo,
o cadastro começa vazio. No C, `fopen` retorna `NULL` e `carregar` retorna 0.

Usei o Codex para ajudar nas partes que faltavam do código, nos testes,
na comparação e na autoavaliação.
