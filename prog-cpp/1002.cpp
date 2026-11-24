// 1002 - Area do Circulo
// LIAC: Calculo o quadrado do raio e multiplico por pi. A saida tem quatro casas.
#include <iomanip>
#include <iostream>

int main() {
    constexpr double pi = 3.14159;
    double raio;
    if (!(std::cin >> raio)) {
        return 0;
    }

    const double raio_ao_quadrado = raio * raio;
    std::cout << std::fixed << std::setprecision(4) << "A=" << raio_ao_quadrado * pi << '\n';
}
