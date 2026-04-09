'''
Problema Beecrowd | 1004
Data: 2026.04.07
Estudante: Gabriela
'''
# Objetivo: somar A e B e seu valor aparecer na variavel PROD

# --- ANÁLISE (LIAC) ---
# Entrada: digitar dois valores inteiros
# Processamento: somar A e B e guardar em PROD
# Saída: aparecer "PROD =" O valor da soma de A e B 

# int(): faz o progama entender que o valor inserido é um numero e não um texto
# input(): le o valor fornecido
# int(input()): le e converte em uma só ordem
A = int(input())
B = int(input())

# O enunciado especifica explicitamente as variaves A, B e PROD - seguir a risca
PROD = A * B

# f-string: coloca o valor de PROD dentro do {}
# Atenção: espaço antes e depois do = obrigatorio
print(f"PROD = {PROD}")