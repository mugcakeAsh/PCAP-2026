// 1178 - Preenchimento de Vetor III
// LIAC: Com o primeiro valor lido, monto cem termos dividindo o anterior por 2.
#include <iomanip>
#include <iostream>
#include <vector>

int main() {
    double inicial;
    if (!(std::cin >> inicial)) {
        return 0;
    }

    std::vector<double> metades;
    metades.reserve(100);
    metades.push_back(inicial);
    while (metades.size() < 100) {
        metades.push_back(metades.back() * 0.5);
    }

    std::cout << std::fixed << std::setprecision(4);
    for (std::size_t pos = 0; pos < metades.size(); pos++) {
        std::cout << "N[" << pos << "] = " << metades[pos] << '\n';
    }
}
