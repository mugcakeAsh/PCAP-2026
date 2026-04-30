'''
Problema Beecrowd | 1021
Data: 2026.04.30
Estudante: Gabriela
'''
# Objetivo: ler um valor e decompor no menor numero possivel

# --- ANÁLISE (LIAC) ---
# Entrada: digitar quantas são cada nota e moeda
# Processamento: separar as notas e moedas e dividir para ver quantas unidades cabem e guardar o resto da divisão
# Saída: mostrar quais e quantos serão as notas e moedas

n, m = input().split(".")

n = int(n)
m = int(m)

n100 = n // 100; n = n % 100
n50 = n // 50; n = n % 50
n20 = n // 20; n = n % 20
n10 = n // 10; n = n % 10
n5 = n // 5; n = n % 5
n2 = n // 2; n = n % 2
n1 = n 

m50 = m // 50; m = m % 50
m25 = m // 25; m = m % 25
m10 = m // 10; m = m % 10
m5 = m // 5; m = m % 5
m1 = m

print("NOTAS: ")
print(f"{n100} nota(s) de R$ 100.00")
print (f"{n50} nota(s) de R$ 50.00")
print (f"{n20} nota(s) de R$ 20.00")
print (f"{n10} nota(s) de R$ 10.00")
print (f"{n5} nota(s) de R$ 5.00")
print (f"{n2} nota(s) de R$ 2.00")
print ("MOEDAS: ")
print (f"{n1} moeda(s) de R$ 1.00")
print (f"{m50} moeda(s) de R$ 0.50")
print (f"{m25} moeda(s) de R$ 0.25")
print (f"{m10} moeda(s) de R$ 0.10")
print (f"{m5} moeda(s) de R$ 0.05")
print (f"{m1} moeda(s) de R$ 0.01")