'''
Problema Beecrowd | 1005
Data: 2026.04.16
Estudante: Gabriela
'''
# Objetivo: falar a media das notas

# --- ANÁLISE (LIAC) ---
# Entrada: as duas notas
# Processamento: multiplica as notas pelo peso delas, soma e divide por 11
# Saída: mostrar media = ...

n1 = float(input())
n2 = float(input())

media = (n1 * 3.5 + n2 * 7.5) / 11

print(f"MEDIA = {media:.5f}")