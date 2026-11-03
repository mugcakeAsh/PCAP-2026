/* Beecrowd 1114 - Senha Fixa. Autor: Gabriela. */
#include <stdio.h>

int main(void) {
    int senha;

    while (scanf("%d", &senha) == 1) {
        if (senha == 2002) {
            printf("Acesso Permitido\n");
            break;
        }
        printf("Senha Invalida\n");
    }
    return 0;
}
