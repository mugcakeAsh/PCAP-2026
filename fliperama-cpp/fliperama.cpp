/*
 * Disciplina: 2026-PCAP, Aula 32
 * Projeto: Fliperama da Gabriela (MeuApp v4.0)
 * Autor: Gabriela
 * LIAC: A escolha do menu indica se devo cadastrar, listar ou jogar.
 * A posicao do apelido tambem indica qual e o contador daquele jogador.
 * A partida conta quando o jogador termina o jogo.
 * Cada linha do CSV guarda esse par para a proxima abertura.
 */

#include <algorithm>
#include <cctype>
#include <charconv>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <limits>
#include <random>
#include <string>
#include <vector>

#define DONO "Gabriela"
constexpr char ARQUIVO[] = "jogadores.csv";

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

int escolher_jogador(const std::vector<std::string> &apelidos, const std::vector<int> &partidas) {
    std::string quem;
    if (!ler_apelido("Apelido de quem vai jogar", quem)) {
        return -1;
    }

    const int posicao = buscar(apelidos, quem);
    if (posicao == -1) {
        std::cout << "Cadastre o jogador antes de jogar.\n";
        return -1;
    }
    if (partidas[posicao] == std::numeric_limits<int>::max()) {
        std::cout << "Esse jogador chegou ao limite de partidas.\n";
        return -1;
    }
    return posicao;
}

bool jogar_adivinhe(const std::vector<std::string> &apelidos, std::vector<int> &partidas,
                    std::mt19937 &sorteador) {
    titulo("ADIVINHE O NUMERO");
    const int jogador = escolher_jogador(apelidos, partidas);
    if (jogador == -1) {
        return false;
    }

    std::uniform_int_distribution<int> numeros(1, 100);
    const int segredo = numeros(sorteador);
    std::cout << "Pensei em um inteiro de 1 a 100.\n";
    int palpite;
    std::size_t tentativas = 0;
    while (ler_numero("Palpite", 1, 100, palpite)) {
        tentativas++;
        if (palpite == segredo) {
            partidas[jogador]++;
            std::cout << apelidos[jogador] << " acertou em " << tentativas << " tentativa(s).\n";
            return true;
        }
        std::cout << (palpite < segredo ? "Tente um valor maior.\n" : "Tente um valor menor.\n");
    }
    return false;
}

bool carregar(std::vector<std::string> &apelidos, std::vector<int> &partidas) {
    std::ifstream entrada(ARQUIVO);
    if (!entrada) {
        std::error_code erro;
        return !std::filesystem::exists(ARQUIVO, erro) && !erro;
    }

    std::string registro;
    while (std::getline(entrada, registro)) {
        if (!registro.empty() && registro.back() == '\r') {
            registro.pop_back();
        }
        const auto virgula = registro.find(',');
        if (virgula == std::string::npos) {
            return false;
        }

        const std::string apelido = registro.substr(0, virgula);
        const char *fim = registro.data() + registro.size();
        int jogadas;
        const auto leitura = std::from_chars(registro.data() + virgula + 1, fim, jogadas);
        if (!apelido_valido(apelido) || leitura.ec != std::errc{} ||
            leitura.ptr != fim || jogadas < 0) {
            return false;
        }
        apelidos.push_back(apelido);
        partidas.push_back(jogadas);
    }
    return entrada.eof() && !entrada.bad();
}

bool salvar(const std::vector<std::string> &apelidos, const std::vector<int> &partidas) {
    // Gravo a nova versao inteira antes de substituir o CSV que ja existe.
    const std::string novo_arquivo = std::string(ARQUIVO) + ".novo";
    std::ofstream saida(novo_arquivo);
    if (!saida) {
        return false;
    }

    const std::size_t qtd = apelidos.size();
    for (std::size_t i = 0; i < qtd; i++) {
        saida << apelidos[i] << ',' << partidas[i] << '\n';
    }
    saida.close();

    std::error_code erro;
    if (saida) {
        std::filesystem::rename(novo_arquivo, ARQUIVO, erro);
        if (!erro) {
            return true;
        }
    }
    std::filesystem::remove(novo_arquivo, erro);
    return false;
}

void mostrar_menu() {
    titulo("FLIPERAMA DA " DONO);
    std::cout << "1 - Adivinhe o Numero\n"
              << "2 - Cadastrar jogador\n"
              << "3 - Listar jogadores\n"
              << "0 - Sair\n";
}

int main() {
    std::mt19937 sorteador(std::random_device{}());
    std::vector<std::string> apelidos;
    std::vector<int> partidas;
    if (!carregar(apelidos, partidas)) {
        std::cerr << "Nao consegui ler o cadastro em " << ARQUIVO << ".\n";
        return 1;
    }
    std::cout << "Jogadores carregados: " << apelidos.size() << ".\n";

    for (;;) {
        mostrar_menu();
        int opcao;
        if (!ler_numero("Sua escolha", 0, 3, opcao) || opcao == 0) {
            break;
        }
        bool mudou = false;
        switch (opcao) {
            case 1:
                mudou = jogar_adivinhe(apelidos, partidas, sorteador);
                break;
            case 2: {
                const auto antes = apelidos.size();
                cadastrar(apelidos, partidas);
                mudou = apelidos.size() != antes;
                break;
            }
            case 3:
                listar(apelidos, partidas);
                break;
        }
        if (mudou && !salvar(apelidos, partidas)) {
            std::cerr << "Nao consegui salvar a ultima mudanca.\n";
            return 1;
        }
    }
    if (!salvar(apelidos, partidas)) {
        std::cerr << "Nao consegui salvar o cadastro ao sair.\n";
        return 1;
    }
    std::cout << "\nAte a proxima!\n";
}
