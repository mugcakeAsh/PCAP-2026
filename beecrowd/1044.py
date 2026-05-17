'''
Problema Beecrowd | 1044
Data: 2026.05.16
Estudante: Gabriela
'''
# Objetivo: ver se os dois numeros sao multiplos

# --- ANÁLISE (LIAC) ---
# Entrada: dois numeros A e B 
# Processamento: identificar maior e maior
# Saída: mostrar a frase "Sao Multiplos" ou "Nao sao Multiplos"

A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")