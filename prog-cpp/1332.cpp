// 1332 - Um-Dois-Tres
// LIAC: Cinco letras indicam three. Se duas letras conferem com two, vale 2.
#include <iostream>
#include <string>

int numero_da_palavra(const std::string &palavra) {
    if (palavra.size() == 5) {
        return 3;
    }

    const std::string dois = "two";
    int iguais = 0;
    for (std::size_t pos = 0; pos < dois.size(); pos++) {
        if (palavra[pos] == dois[pos]) {
            iguais++;
        }
    }
    return iguais >= 2 ? 2 : 1;
}

int main() {
    int quantidade;
    if (!(std::cin >> quantidade)) {
        return 0;
    }

    std::string palavra;
    for (int caso = 0; caso < quantidade && std::cin >> palavra; caso++) {
        std::cout << numero_da_palavra(palavra) << '\n';
    }
}
