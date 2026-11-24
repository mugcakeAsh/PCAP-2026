// 1174 - Selecao em Vetor I
// LIAC: Guardo os valores reais e exibo so as posicoes com valor <= 10.
#include <iomanip>
#include <iostream>
#include <vector>

void mostrar_selecao(const std::vector<double> &valores) {
    std::cout << std::fixed << std::setprecision(1);
    for (std::size_t pos = 0; pos < valores.size(); pos++) {
        if (valores[pos] <= 10.0) {
            std::cout << "A[" << pos << "] = " << valores[pos] << '\n';
        }
    }
}

int main() {
    std::vector<double> valores(100);
    for (double &valor : valores) {
        if (!(std::cin >> valor)) {
            return 0;
        }
    }
    mostrar_selecao(valores);
}
