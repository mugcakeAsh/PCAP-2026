# Quiz de Informática

Jogo criado para o Fliperama da Gabriela. Ele abre pela opção `[4]` do menu.

## A regra

O Quiz apresenta três perguntas básicas de informática, cada uma com três
alternativas. Uma resposta certa vale um ponto. Para vencer, o jogador precisa
acertar pelo menos duas perguntas.

## Como jogar

1. Abra o terminal dentro da pasta `fliperama`;
2. Execute `python3 main.py`;
3. Escolha a opção `[4]`;
4. Digite `1`, `2` ou `3` para responder cada pergunta.

## O que foi reaproveitado

| Peça | Módulo | Onde aparece | Utilidade |
|---|---|---|---|
| `titulo()` | `telas.py` | `meujogo.py`, linhas 40 e 65–68 | mostra o nome e o resultado do Quiz |
| `linha()` | `telas.py` | `meujogo.py`, linha 61 | separa as perguntas |
| `ler_opcao()` | `modulos.py` | `meujogo.py`, linha 53 | aceita somente as alternativas 1, 2 e 3 |
| contador do jogo | `placar.py` | `main.py`, linha 80 | registra quantas vezes o Quiz foi aberto |
| `buscar()` | `jogadores.py` | `main.py`, linhas 82–87 | encontra a ficha de quem está jogando |

## Exemplo de execução

```text
============================================
            QUIZ DE INFORMATICA
============================================
Pergunta 1 de 3
Qual componente executa as instrucoes do computador?
[1] Teclado
[2] Processador
[3] Monitor
Resposta: 2
Resposta correta!
```

## Limitação

O Quiz possui somente três perguntas fixas e ainda não sorteia perguntas novas.
