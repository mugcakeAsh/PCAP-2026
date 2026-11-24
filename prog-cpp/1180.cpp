// 1180 - Menor e Posicao
// LIAC: Percorro o vector de inteiros e mostro o menor com o indice dele.
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    int quantidade;
    if (!(std::cin >> quantidade) || quantidade <= 0) {
        return 0;
    }

    std::vector<int> valores(quantidade);
    for (int &valor : valores) {
        std::cin >> valor;
    }
    const auto menor = std::min_element(valores.begin(), valores.end());
    std::cout << "Menor valor: " << *menor << '\n';
    std::cout << "Posicao: " << menor - valores.begin() << '\n';
}
