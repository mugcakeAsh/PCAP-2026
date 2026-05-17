'''
Problema Beecrowd | 1035
Data: 2026.05.17
Estudante: Gabriela
'''
# Objetivo: dizer se os valores sao ou não aceitos

# --- ANÁLISE (LIAC) ---
# Entrada: digitar os numeros a, b, c, d
# Processamento: fazer as contas e ver se os numeros são ou não aceitos
# Saída: mostrar valores aceitos ou valores nao aceitos

A, B, C, D = map(int, input().split())

if B > C and D > A and C + D > A + B and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")