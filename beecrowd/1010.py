'''
Problema Beecrowd | 1010
Data: 2026.05.17
Estudante: Gabriela
'''
# Objetivo: somar o valor total da compra

# --- ANÁLISE (LIAC) ---
# Entrada: 6 valores, 3 em cada linha
# Processamento: multiplicar o valor b, c da primeira e da segunda linha (separadamente) e somalos
# Saída: mostrar "valor a pagar: ..."

cod1, qtd1, val1 = input().split()

qtd1 = int(qtd1)
val1 = float(val1)

cod2, qtd2, val2 = input().split()

qtd2 = int(qtd2)
val2 = float(val2)

total1 = qtd1 * val1
total2 = qtd2 * val2
total = total1 + total2

print(f"VALOR A PAGAR: R$ {total:.2f}")
