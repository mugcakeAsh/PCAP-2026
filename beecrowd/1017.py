'''
Problema Beecrowd | 1017
Data: 2026.05.17
Estudante: Gabriela
'''
# Objetivo: descobrir quantos litros de combustivel foram usados

# --- ANÁLISE (LIAC) ---
# Entrada: horas da viagem e velocidade do carro
# Processamento: calcular a distancia percorrida e dividir por 12
# Saída: mostrar os litros gastos com 3 casas decimais

horas = int(input())
km_h = int(input())

km = horas * km_h

gasto = km / 12

print(f"{gasto:.3f}")