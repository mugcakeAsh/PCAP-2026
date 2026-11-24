// 1011 - Esfera
// LIAC: Uso o raio ao cubo na formula do volume e fixo tres casas na resposta.
#include <iomanip>
#include <iostream>

int main() {
    int raio;
    if (!(std::cin >> raio)) {
        return 0;
    }

    constexpr double coeficiente = 4.0 * 3.14159 / 3.0;
    const double raio_ao_cubo = static_cast<double>(raio) * raio * raio;
    std::cout << "VOLUME = " << std::fixed << std::setprecision(3)
              << coeficiente * raio_ao_cubo << '\n';
}
