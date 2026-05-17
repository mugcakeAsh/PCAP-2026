'''
Problema Beecrowd | 1013
Data: 2026.05.17
Estudante: Gabriela
'''
# Objetivo: descobrir qual é o maior entre três números

# --- ANÁLISE (LIAC) ---
# Entrada: receber três números inteiros
# Processamento: comparar os valores para encontrar o maior
# Saída: exibir o maior número com a mensagem "eh o maior"

A, B, C = map(int, input().split())

maior = A

if B > maior:
    maior = B

if C > maior:
    maior = C

print(f"{maior} eh o maior")