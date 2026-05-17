'''
Problema Beecrowd | 1047
Data: 2026.05.16
Estudante: Gabriela
'''
# Objetivo: calcular a duração de um jogo em horas e minutos

# --- ANÁLISE (LIAC) ---
# Entrada: hora e minuto inicial e final
# Processamento: processar quanto tempo o jogo durou
# Saída: mostrar o "o jogo durou ... horas e ... minutos"

hi, mi, hf, mf = map(int, input().split())

tim = (hi * 60) + mi
tfm = (hf * 60) + mf

if tim > tfm:
    ttm = (tfm - tim) + (24 * 60)
else: 
    ttm = tfm - tim

if ttm == 0:
    ttm = 24 * 60

print (f"O JOGO DUROU {ttm // 60} HORA(S) E {ttm % 60} MINUTO(S)")