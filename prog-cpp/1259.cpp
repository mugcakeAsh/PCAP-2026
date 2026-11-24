// 1259 - Pares e Impares Ordenados
// LIAC: Ordeno o mesmo vector com uma regra que poe os pares primeiro.
#include <algorithm>
#include <iostream>
#include <vector>

bool vem_antes(int esquerda, int direita) {
    const bool esquerda_par = esquerda % 2 == 0;
    const bool direita_par = direita % 2 == 0;
    if (esquerda_par != direita_par) {
        return esquerda_par;
    }
    if (esquerda_par) {
        return esquerda < direita;
    }
    return esquerda > direita;
}

int main() {
    int quantidade;
    if (!(std::cin >> quantidade) || quantidade < 0) {
        return 0;
    }

    std::vector<int> numeros(quantidade);
    for (int &numero : numeros) {
        std::cin >> numero;
    }
    std::sort(numeros.begin(), numeros.end(), vem_antes);
    for (int numero : numeros) {
        std::cout << numero << '\n';
    }
}
