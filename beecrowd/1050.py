'''
Problema Beecrowd | 1050
Data: 2026.05.14
Estudante: Gabriela
'''
# Objetivo: ler um codigo ddd e falar de qual cidade ele é

# --- ANÁLISE (LIAC) ---
# Entrada: digitar nuero do ddd
# Processamento: comparar o ddd com uma das cidades da tabela
# Saída: falar a qual cidade o ddd percentence, ou falar se o dd nao estiver na tabela

DDD = int(input())

if DDD == 61:
 print("Brasilia")
elif DDD == 71:
 print("Salvador")
elif DDD == 11:
 print("Sao Paulo")
elif DDD == 21:
 print("Rio de Janeiro")
elif DDD == 32:
 print("Juiz de Fora")
elif DDD == 19:
 print("Campinas")
elif DDD == 27:
 print("Vitoria")
elif DDD == 31:
 print("Belo Horizonte")
else:
 print("DDD nao cadastrado")