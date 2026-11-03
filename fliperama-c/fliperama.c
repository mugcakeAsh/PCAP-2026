/*
Disciplina: 2026-PCAP
Projeto : Fliperama em C
Autor : Gabriela
LIAC : O menu cadastra e lista jogadores e abre o Adivinhe.
Os apelidos e as partidas ficam em dois vetores.
Ao sair, o cadastro vai para um arquivo e volta na proxima abertura.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define DONO "Gabriela"
#define CAPACIDADE 50
#define TAM_APELIDO 20
#define ARQUIVO "jogadores.csv"

void linha() {
    printf
    ("======================================\n");

}

void titulo(char texto[]){
    linha();
    printf(" %s\n",texto);
    linha();
}

int ler_numero(char mensagem[], int minimo, int maximo) {
    int numero, lidos;

    printf(" %s:", mensagem);
    lidos = scanf("%d", &numero);
    while (lidos != 1 || numero < minimo || numero > maximo){
        if (lidos == EOF) {
            printf("\nEntrada encerrada.\n");
            exit(EXIT_SUCCESS);
        }
        if (lidos !=1){
        scanf("%*s");
    }

    printf("Opcao invalida! Tente novamente: ");
    lidos = scanf("%d", &numero);
    }

    return numero;

}

void ler_texto(char mensagem[], char destino[]) {
    printf("%s: ", mensagem);
    scanf("%19s", destino);
}

int buscar(char apelidos[][TAM_APELIDO], int qtd, char procurado[]) {
    int i;

    for (i = 0; i < qtd; i++) {
        if (strcmp(apelidos[i], procurado) == 0) {
            return i;
        }
    }
    return -1;
}

int cadastrar(char apelidos[][TAM_APELIDO], int partidas[], int qtd) {
    char novo[TAM_APELIDO];

    titulo("NOVO JOGADOR");
    if (qtd >= CAPACIDADE) {
        printf("Sem espaco no cadastro. O limite foi atingido.\n");
        return qtd;
    }
    ler_texto("Apelido (sem espacos)", novo);

    if (strchr(novo, ',') != NULL) {
        printf("Use um apelido sem virgula.\n");
        return qtd;
    }

    if (buscar(apelidos, qtd, novo) != -1) {
        printf("Esse apelido ja esta cadastrado. \n");
        return qtd;
    }

    strcpy(apelidos[qtd], novo);
    partidas[qtd] = 0;
    printf("Jogador %s cadastrado. \n", novo);
    return qtd + 1;
}

void listar(char apelidos[][TAM_APELIDO], int partidas[], int qtd) {
    int i;

    titulo("JOGADORES CADASTRADOS");
    if (qtd == 0) {
        printf("Nenhum jogador cadastrado ainda. \n");
    }
    for (i = 0; i < qtd; i++) {
        printf("%s | %d partidas\n", apelidos[i], partidas[i]);
    }
}

void jogar_adivinhe(char apelidos[][TAM_APELIDO], int partidas[], int qtd) {
    char quem[TAM_APELIDO];
    int posicao, segredo, palpite, tentativas;

    titulo("ADIVINHE O NUMERO");
    ler_texto("Apelido de quem vai jogar", quem);
    posicao = buscar(apelidos, qtd, quem);
    if (posicao == -1) {
        printf("Primeiro cadastre esse jogador.\n");
        return;
    }

    partidas[posicao] = partidas[posicao] + 1;
    segredo = rand() % 100 + 1;
    printf("Tente descobrir o numero de 1 a 100.\n");
    palpite = ler_numero("Palpite", 1, 100);
    tentativas = 1;
    while (palpite != segredo) {
        if (palpite < segredo) {
            printf("O numero e maior.\n");
        } else {
            printf("O numero e menor.\n");
        }
        palpite = ler_numero("Palpite", 1, 100);
        tentativas = tentativas + 1;
    }
    printf("Acertou em %d tentativas, %s!\n", tentativas, quem);
}

void salvar(char apelidos[][TAM_APELIDO], int partidas[], int qtd) {
    FILE *arquivo = fopen(ARQUIVO, "w");
    int i;
    if (arquivo == NULL) {
        perror("Nao deu para salvar o cadastro");
        exit(EXIT_FAILURE);
    }
    for (i = 0; i < qtd; i++) {
        fprintf(arquivo, "%s,%d\n", apelidos[i], partidas[i]);
    }
    if (fclose(arquivo) != 0) {
        perror("Erro ao salvar o arquivo");
        exit(EXIT_FAILURE);
    }
}

int carregar(char apelidos[][TAM_APELIDO], int partidas[]) {
    FILE *arquivo = fopen(ARQUIVO, "r");
    int qtd = 0;
    if (arquivo == NULL) {
        return 0;
    }
    while (qtd < CAPACIDADE &&
           fscanf(arquivo, "%19[^,],%d\n", apelidos[qtd], &partidas[qtd]) == 2) {
        qtd = qtd + 1;
    }
    fclose(arquivo);
    return qtd;
}

void mostrar_menu() {
    linha();
    printf("      FLIPERAMA DA %s\n", DONO);
    linha();
    printf("[1] Adivinhe o Numero\n");
    printf("[2] Cadastrar Jogador\n");
    printf("[3] Listar Jogadores\n");
    printf("[0] Sair\n");
    linha();

}

    int main() {
        char apelidos[CAPACIDADE][TAM_APELIDO];
        int partidas[CAPACIDADE];
        int qtd, opcao;

        srand((unsigned int)time(NULL));
        qtd = carregar(apelidos, partidas);

        mostrar_menu();
        opcao = ler_numero("Sua escolha", 0, 3);
        while (opcao != 0){
            if (opcao == 1){
                jogar_adivinhe(apelidos, partidas, qtd);
            }else if (opcao == 2) {
                qtd = cadastrar(apelidos, partidas, qtd);
            }else {
                listar(apelidos, partidas, qtd);
            }
            mostrar_menu();
            opcao = ler_numero("Sua escolha", 0, 3);
        }

        salvar(apelidos, partidas, qtd);
        titulo("Ate a proxima!");
        return 0;
    }
