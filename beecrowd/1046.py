'''
Problema: beecrowd | 1046
Data: 2026.05.17
Estudante: Gabriela
'''
# Objetivo: calcular a duração de um jogo em horas

# --- ANALISE (LIAC) ---
# Entrada: hora inicial e hora final
# Processamento: calcular quanto tempo o jogo durou
# Saída: mostrar a duração do jogo em horas

hi, hf = map(int, input().split())

tim = hi * 60
tfm = hf * 60

if tim > tfm:
    ttm = (tfm - tim) + (24 * 60)
else:
    ttm = tfm - tim

if ttm == 0:
    ttm = 24 * 60

print(f"O JOGO DUROU {ttm // 60} HORA(S)")