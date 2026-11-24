/*
 * Disciplina: 2026-PCAP, Aula 32
 * Projeto: Fliperama da Gabriela (MeuApp v4.0)
 * Autor: Gabriela
 * LIAC: A escolha do menu indica se devo cadastrar, listar ou jogar.
 * A posicao do apelido tambem indica qual e o contador daquele jogador.
 */

#include <algorithm>
#include <cctype>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

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

bool apelido_valido(const std::string &apelido) {
    const bool tem_separador = std::any_of(apelido.begin(), apelido.end(), [](unsigned char c) {
        return c == ',' || std::isspace(c);
    });
    return !apelido.empty() && !tem_separador;
}

bool ler_apelido(const std::string &pergunta, std::string &apelido) {
    std::cout << pergunta << ": ";
    if (!std::getline(std::cin, apelido)) {
        return false;
    }
    if (!apelido_valido(apelido)) {
        std::cout << "Digite um apelido sem espacos e sem virgula.\n";
        return false;
    }
    return true;
}

int buscar(const std::vector<std::string> &apelidos, const std::string &quem) {
    const auto encontrado = std::find(apelidos.begin(), apelidos.end(), quem);
    return encontrado == apelidos.end() ? -1 : static_cast<int>(encontrado - apelidos.begin());
}

void cadastrar(std::vector<std::string> &apelidos, std::vector<int> &partidas) {
    titulo("NOVO JOGADOR");
    std::string novo;
    if (!ler_apelido("Apelido", novo)) {
        return;
    }
    apelidos.push_back(novo);
    partidas.push_back(0);
    std::cout << "Cadastro feito para " << novo << ".\n";
}

void listar(const std::vector<std::string> &apelidos, const std::vector<int> &partidas) {
    titulo("JOGADORES CADASTRADOS");
    const std::size_t qtd = apelidos.size();
    if (qtd == 0) {
        std::cout << "O cadastro esta vazio.\n";
        return;
    }
    for (std::size_t i = 0; i < qtd; i++) {
        std::cout << apelidos[i] << " - " << partidas[i] << " partida(s)\n";
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
    std::vector<std::string> apelidos;
    std::vector<int> partidas;
    for (;;) {
        mostrar_menu();
        int opcao;
        if (!ler_numero("Sua escolha", 0, 3, opcao) || opcao == 0) {
            break;
        }
        switch (opcao) {
            case 1:
                std::cout << "Adivinhe o Numero\n";
                break;
            case 2:
                cadastrar(apelidos, partidas);
                break;
            case 3:
                listar(apelidos, partidas);
                break;
        }
    }
    std::cout << "\nAte a proxima!\n";
}
