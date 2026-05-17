'''
Problema Beecrowd | 1006
Data: 2026.05.16
Estudante: Gabriela
'''
# Objetivo: falar a media das notas

# --- ANÁLISE (LIAC) ---
# Entrada: as tres notas
# Processamento: soma as 3 notas, multiplica pelo peso delas e divide por 3
# Saída: mostrar media = ...

n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 * 2 + n2 * 3 + n3 * 5) / 10

print(f"MEDIA = {media:.1f}")