/*
 * Disciplina: 2026-PCAP, Aula 32
 * Projeto: Fliperama da Gabriela (MeuApp v4.0)
 * Autor: Gabriela
 * LIAC: Leio a escolha do menu, confiro a faixa e abro a tela pedida.
 */

#include <iostream>
#include <limits>
#include <string>

#define DONO "Gabriela"

void titulo(const std::string &texto) {
    std::cout << "\n=== " << texto << " ===\n";
}

bool ler_numero(const std::string &pergunta, int minimo, int maximo, int &numero) {
    while (true) {
        std::cout << pergunta << ": ";
        if (std::cin >> numero) {
            std::string resto_da_linha;
            std::getline(std::cin, resto_da_linha);
            if (numero >= minimo && numero <= maximo &&
                resto_da_linha.find_first_not_of(" \t\r") == std::string::npos) {
                return true;
            }
        } else {
            if (std::cin.eof() || std::cin.bad()) {
                return false;
            }
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
        if (!std::cin.good()) {
            return false;
        }
        std::cout << "Opcao invalida. Use um numero de " << minimo << " a " << maximo << ".\n";
    }
}

void mostrar_menu() {
    titulo("FLIPERAMA DA " DONO);
    std::cout << "1 - Adivinhe o Numero\n"
              << "2 - Cadastrar jogador\n"
              << "3 - Listar jogadores\n"
              << "0 - Sair\n";
}

int main() {
    for (;;) {
        mostrar_menu();
        int opcao;
        if (!ler_numero("Sua escolha", 0, 3, opcao) || opcao == 0) {
            break;
        }
        std::cout << "Escolha " << opcao << " lida.\n";
    }
    std::cout << "\nAte a proxima!\n";
}
