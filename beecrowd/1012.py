'''
Problema Beecrowd | 1012
Data: 2026.05.16
Estudante: Gabriela
'''
# Objetivo: falar a area do triangulo, circulo, trapezio, quadrado e retangulo

# --- ANÁLISE (LIAC) ---
# Entrada: digitar 3 valor (a, b, c)
# Processamento: achar o valor da areas das formas pelos valores a, b e c
# Saída: mostrar "triangulo: ...", "circulo: ...", "trapezio: ...", "quadrado: ..." e "retangulo: ..."

A,B,C = map(float, input().split())
pi = 3.14159

print(f"TRIANGULO: {A*C/2.0:.3f}")
print(f"CIRCULO: {pi*C*C:.3f}")
print(f"TRAPEZIO: {(A+B)*C/2.0:.3f}")
print(f"QUADRADO: {B*B:.3f}")
print(f"RETANGULO: {A*B:.3f}")