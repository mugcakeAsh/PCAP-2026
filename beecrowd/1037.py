'''
Problema Beecrowd | 1037
Data: 2026.05.16
Estudante: Gabriela
'''
# Objetivo: ler um valor e falar em qual intervalo ele se encontra

# --- ANÁLISE (LIAC) ---
# Entrada: um numero decimal
# Processamento: ver em qual dos intervalos o valor esta
# Saída: mostrar o intervalo correspondente ou fora de intervalo

valor = float(input())

if 0 <= valor <= 25:
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")