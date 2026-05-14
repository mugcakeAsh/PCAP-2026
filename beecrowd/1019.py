'''
Problema Beecrowd | 1019
Data: 2026.05.14
Estudante: Gabriela
'''
# Objetivo: convertar segundos em horas, minutos e segundos

# --- ANÁLISE (LIAC) ---
# Entrada: digitar o numero de segundos
# Processamento: extrair horas, minutos e segundos em divisao inteira e modulo
# Saída: mostrar horas:minutos:segundos sem zeros 

N = int(input())
h = N // 3600
N = N % 3600
m = N // 60
s = N % 60

print(f"{h}:{m}:{s}")