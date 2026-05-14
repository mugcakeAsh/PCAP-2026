'''
Problema Beecrowd | 1007
Data: 2026.05.14
Estudante: Gabriela
'''
# Objetivo: ler os numeros digitados e calcular a diferença

# --- ANÁLISE (LIAC) ---
# Entrada: digitar o valor de A, B, C e D
# Processamento: faz a diferença do A.B com o C.D
# Saída: mostrar DIFERENÇA = valor

A = int(input())
B = int(input())
C = int(input())
D = int(input())

dif = (A * B) - (C * D)

print(f"DIFERENCA = {dif}")