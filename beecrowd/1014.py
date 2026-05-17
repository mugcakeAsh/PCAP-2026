'''
Problema: beecrowd | 1014
Data: 2026.05.17
Estudante: Gabriela
'''
# Objetivo: ver o consumo medio de um automovel pelos quilometros percorridos e litros de gasolinas gastos

#--- ANALISE (LIAC) ---
# Entrada: digitar os km e os litros de gasolina
# Processamento: divide os km pelos litros de gasolina e da a media do consumo
# Saida: mostrar consumo medio

X = int(input())

Y = float(input())

consumo = X / Y

print(f"{consumo:.3f} km/l")