'''
Problema Beecrowd | 1009
Data: 2026.04.16
Estudante: Gabriela
'''
# Objetivo: falar o nome, somar o salario e 15% das vendas que esse mesmo funcionario fez

# --- ANÁLISE (LIAC) ---
# Entrada: o valor do salario e das vendas
# Processamento: vendas * 0.15 + salario fixo =total
# Saída: falar o total que o funcinario vai receber

n = input()
s = float(input())
v = float(input())

c = v * 0.15

st = s + c

print(f"TOTAL = R$ {st:.2f}")