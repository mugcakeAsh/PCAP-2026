// 1004 - Produto Simples
// LIAC: Recebo dois valores inteiros e imprimo o produto com o rotulo PROD.
#include <iostream>

int main() {
    long long fator1, fator2;
    if (std::cin >> fator1 >> fator2) {
        const long long produto = fator1 * fator2;
        std::cout << "PROD = " << produto << '\n';
    }
}
