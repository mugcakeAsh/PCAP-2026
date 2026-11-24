// 1551 - Frase Completa
// LIAC: Procuro cada letra do alfabeto na frase e conto quais aparecem.
#include <iostream>
#include <string>

int main() {
    int total_frases;
    if (!(std::cin >> total_frases)) {
        return 0;
    }

    std::string frase;
    std::getline(std::cin, frase); // Consome o fim da linha do total.
    for (int caso = 0; caso < total_frases && std::getline(std::cin, frase); caso++) {
        int letras = 0;
        for (char letra = 'a'; letra <= 'z'; letra++) {
            if (frase.find(letra) != std::string::npos) {
                letras++;
            }
        }

        if (letras < 13) {
            std::cout << "frase mal elaborada\n";
        } else if (letras < 26) {
            std::cout << "frase quase completa\n";
        } else {
            std::cout << "frase completa\n";
        }
    }
}
