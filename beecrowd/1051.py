'''
Problema Beecrowd | 1051
Data: 2026.05.17
Estudante: Gabriela
'''
# Objetivo: mostrar o valor do imposto de renda que deve ser pago

# --- ANÁLISE (LIAC) ---
# Entrada: colocar o valor do salario
# Processamento: calcula o imposto de renda
# Saída: mostrar o "R$ ..." ou "Isento"

salario = float(input())

imposto = 0

if salario <= 2000:
    print("Isento")
else:
    if salario <= 3000: 
        imposto += (salario - 2000)*.08 
    elif salario <= 4500:
        imposto += 1000*.08
        imposto += (salario - 3000)*.18
    else:
        imposto += 1000*.08
        imposto += 1500*.18
        imposto += (salario - 4500)*.28

    print(f"R$ {imposto:.2f}")