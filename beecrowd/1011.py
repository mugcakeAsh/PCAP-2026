'''
Problema Beecrowd | 1011
Data: 2026.04.10
Estudante: Gabriela
'''
# Objetivo: mostrar o volume de uma esfera

# --- ANÁLISE (LIAC) ---
# Entrada: a entrada é o raio da esfera
# Processamento: aplicar a formula do volume na esfera
# Saída: mostrar o resultado "VOLUME = valor"

R = float(input())

pi = 3.14159

V = (4 / 3.0) * pi * R ** 3

print(f"VOLUME = {V:.3f}")

