// 1173 - Preenchimento de Vetor I
// LIAC: Acrescento o dobro do ultimo valor ate completar dez numeros.
#include <iostream>
#include <vector>

int main() {
    int primeiro;
    if (!(std::cin >> primeiro)) {
        return 0;
    }

    std::vector<int> numeros{primeiro};
    while (numeros.size() < 10) {
        numeros.push_back(2 * numeros.back());
    }

    for (std::size_t pos = 0; pos < numeros.size(); pos++) {
        std::cout << "N[" << pos << "] = " << numeros[pos] << '\n';
    }
}
