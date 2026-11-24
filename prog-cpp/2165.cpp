// 2165 - Tuitando
// LIAC: Os espacos entram na contagem, entao leio a mensagem com getline.
#include <iostream>
#include <string>

int main() {
    constexpr int limite = 140;
    std::string texto;
    if (!std::getline(std::cin, texto)) {
        return 0;
    }

    if (texto.size() > limite) {
        std::cout << "MUTE\n";
    } else {
        std::cout << "TWEET\n";
    }
}
