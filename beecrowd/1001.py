'''
Problema Beecrowd | 1001
Data: 2026.02.01
Estudante: Gabriela
'''
# Objetivo: somar A e B e seu valor aparecer na variavel X

# --- ANÁLISE (LIAC) ---
# Entrada: digitar dois valores inteiros
# Processamento: somar A e B e guardar em X
# Saída: aparecer "X =" o valor da soma de A e B

# int(): faz o progama entender que o valor inserido é um numero e não um texto
# input(): le o valor fornecido
# int(input()): le e converte em uma só ordem
A = int(input())
B = int(input())

# O enunciado especifica explicitamente as variaves A, B e X - seguir a risca
X = A + B

# f-string: coloca o valor de X dentro do {}
# Atenção: espaço antes e depois do = obrigatorio
print(f"X = {X}")