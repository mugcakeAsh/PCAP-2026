// 1049 - Animal
// LIAC: A classe e o alimento separam os animais em cada grupo.
#include <iostream>
#include <string>

const char *identificar(const std::string &grupo, const std::string &classe,
                       const std::string &alimento) {
    if (grupo == "vertebrado" && classe == "ave") {
        return alimento == "carnivoro" ? "aguia" : "pomba";
    }
    if (grupo == "vertebrado") {
        return alimento == "herbivoro" ? "vaca" : "homem";
    }
    if (classe == "inseto") {
        return alimento == "herbivoro" ? "lagarta" : "pulga";
    }
    return alimento == "onivoro" ? "minhoca" : "sanguessuga";
}

int main() {
    std::string grupo, classe, alimento;
    if (std::cin >> grupo >> classe >> alimento) {
        std::cout << identificar(grupo, classe, alimento) << '\n';
    }
}
