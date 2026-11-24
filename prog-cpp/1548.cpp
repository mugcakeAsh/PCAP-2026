// 1548 - Fila do Recreio
// LIAC: Comparo a fila inicial com uma fila em ordem decrescente de notas.
#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

int lugares_mantidos(const std::vector<int> &original) {
    auto por_nota = original;
    std::sort(por_nota.begin(), por_nota.end(), std::greater<int>());

    int mantidos = 0;
    for (std::size_t lugar = 0; lugar < original.size(); lugar++) {
        if (original[lugar] == por_nota[lugar]) {
            mantidos++;
        }
    }
    return mantidos;
}

int main() {
    int quantidade_de_filas;
    if (!(std::cin >> quantidade_de_filas)) {
        return 0;
    }

    for (int caso = 0; caso < quantidade_de_filas; caso++) {
        int alunos;
        std::cin >> alunos;
        std::vector<int> fila(alunos);
        for (int &nota : fila) {
            std::cin >> nota;
        }
        std::cout << lugares_mantidos(fila) << '\n';
    }
}
