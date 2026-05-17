'''
Problema Beecrowd | 1020
Data: 2026.05.16
Estudante: Gabriela
'''
# Objetivo: mostrar quantos anos, meses e dias baseado nos dias

# --- ANÁLISE (LIAC) ---
# Entrada: digitar dias
# Processamento: extrair anos, meses e dias com base no numero de dias informado
# Saída: mostrar "... ano(s)", "... mes(es)", "... dia(s)"

N = int(input())
a = N // 365
N = N % 365
m = N // 30
d = N % 30

print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")