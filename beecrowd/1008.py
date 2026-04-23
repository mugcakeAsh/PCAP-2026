'''
Problema Beecrowd | 1008
Data: 2026.04.16
Estudante: Gabriela
'''
# Objetivo: falar o numero do funcionario e o salario

# --- ANÁLISE (LIAC) ---
# Entrada: numero do funcionario, numero de horas trabalhadas e o valor que ele recebe por hora
# Processamento: horas trabalhadas * salario por hora = salary
# Saída: mostrar o nome do funcionario e seu salario total

N = int(input())
H = int(input())
V = float(input())

SAL = H * V

print(f"NUMBER = {N}")
print(f"SALARY = U$ {SAL:.2f}")