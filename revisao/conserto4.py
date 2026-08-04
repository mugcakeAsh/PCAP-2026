jogada = input("pedra, papel ou tesoura? ").lower().strip()
if jogada == "pedra" or jogada == "papel" or jogada == "tesoura":
    print("Jogada válida!", jogada)
else:
    print("Jogada inválida!")