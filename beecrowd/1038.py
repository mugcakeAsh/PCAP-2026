'''
Problema Beecrowd | 1038
Data: 2026.05.16
Estudante: Gabriela
'''
# Objetivo: 

# --- ANÁLISE (LIAC) ---
# Entrada: 
# Processamento: 
# Saída: 


codigo, quantidade = map(int, input().split())

if codigo == 1:
 codigo = int(4.00)
elif codigo == 2:
 codigo = float(4.50)
elif codigo == 3:
 codigo = int(5.00)
elif codigo == 4:
 codigo = int(2.00)
elif codigo == 5:
 codigo = float(1.50)

t = codigo * quantidade

print(f"Total: R$ {t:.2f}")