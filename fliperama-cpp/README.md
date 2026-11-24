# Fliperama da Gabriela em C++

MeuApp v4.0 · PCAP · Aula 32

## O que é

O fliperama tem dois jogos: Adivinhe o Número e o Quiz de Informática da Atividade 15. O cadastro guarda quantas partidas cada pessoa terminou, mesmo que ela perca o Quiz. O ranking mostra quem jogou mais.

O menu veio do [Fliperama em C](../fliperama-c). As três perguntas do Quiz vieram do [jogo que eu já tinha em Python](../fliperama/meujogo.py).

## Como compilar e rodar

```bash
cd fliperama-cpp
g++ -Wall fliperama.cpp -o fliperama
./fliperama
```

| Opção | O que faz |
|---|---|
| 1 | Adivinhar o número entre 1 e 100 |
| 2 e 3 | Cadastrar ou listar jogadores |
| 4 | Jogar o Quiz. Dois acertos em três perguntas dão a vitória. |
| 5 e 6 | Mudar um apelido ou excluir um jogador após confirmação |
| 7 | Ver o ranking por partidas |
| 0 | Salvar e sair |

Use apelidos únicos, sem espaços nem vírgulas. O programa diferencia maiúsculas de minúsculas. Rode dentro de `fliperama-cpp` para usar o CSV dessa versão.

Trecho do terminal após uma partida de teste do Quiz:

```text
Total de acertos: 3 de 3.

=== VOCE VENCEU O QUIZ! ===
```

```text
=== RANKING POR PARTIDAS ===
1. Nina - 1 partida(s)
```

## Arquivos

- `fliperama.cpp` tem o menu, as operações do cadastro e os dois jogos.
- `jogadores.csv` guarda um apelido e um total de partidas por linha. Os três registros iniciais vieram do Fliperama em C.

Ao abrir, o programa mostra quantos jogadores carregou. Salva após cadastrar, alterar ou excluir um jogador, após cada partida completa e ao sair.

## C × C++: o que mudou

| Operação | [Versão em C](../fliperama-c/fliperama.c) | [Versão em C++](fliperama.cpp) |
|---|---|---|
| Ler uma opção | Linha 36, `scanf("%d", &numero)`. | Linhas 34–39, `cin >> numero` e `getline` para conferir o resto da entrada. |
| Guardar um apelido | Linha 90, `strcpy(apelidos[qtd], novo)`. | Linhas 89–90, `push_back` no apelido e na contagem de partidas. |
| Encontrar um jogador | Linha 63, `strcmp` compara os apelidos. | Linhas 75–76, `std::find` usa a igualdade de `string` e o resultado vira uma posição. |
| Cadastrar | Linhas 70 e 93, a função recebe `qtd` e devolve o novo total. | Linha 79, `void cadastrar` recebe os dois `vectors` por referência. |
| Quando o cadastro enche | Linhas 16 e 74, limite de 50 pessoas e teste de lotação. | Linhas 89–90, os `vectors` aumentam de tamanho a cada cadastro. |
| Gravar em arquivo | Linha 138, `fopen` abre o CSV. | Linhas 301–309, `ofstream` grava a nova versão do CSV. |

## O que o C++ decidiu por mim

Ao cadastrar, `push_back` abre espaço para o apelido e ajusta o tamanho do `vector`. Eu consulto a quantidade com `size()`. A `string` cuida do espaço necessário para o texto.

`cadastrar` passou a devolver `void` porque o menu e a função enxergam os mesmos `vectors` por referência. Para decidir se precisa salvar, o menu confere se o tamanho aumentou nas linhas 358–360.

## Autoavaliação

| Critério | Conceito esperado | Evidência |
|---|---|---|
| 1. Estrutura, compilação e Git | A | `fliperama.cpp`, linhas 1–8 e 24, cabeçalho e nome. A compilação com `-Wall` saiu sem avisos. `.gitignore`, linhas 8–12, e commits das fases da Aula 32. |
| 2. Cadastro e referências | A | `fliperama.cpp`, linhas 74–101 e 105–178, busca, duplicatas, edição, exclusão confirmada e ranking sem reordenar o cadastro. |
| 3. Jogos e partidas | A | `fliperama.cpp`, linhas 198–220 e 229–265, dois jogos que contam partidas ao terminar. |
| 4. Persistência | A | `fliperama.cpp`, linhas 268–322 e 340–344, leitura e gravação do CSV com contagem ao abrir. Linhas 379–387, gravação após alterações e ao sair. |
| 5. Documentação e comparação | A | Este README registra seis comparações entre os códigos e mostra a execução de um teste do Quiz. |

## O que continua comigo

- Onde usar referência. Na linha 79, os dois parâmetros têm `&` porque o cadastro precisa mudar os `vectors` do menu.
- Como manter cada apelido ligado à contagem certa. Nas linhas 153–154, retiro o mesmo índice dos dois `vectors`. Na linha 170, ordeno os índices para fazer o ranking sem mexer nos pares.

O código em C++, os testes e o rascunho de autoavaliação foram preparados com ajuda do Codex.
