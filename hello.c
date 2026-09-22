/* 
Comentário de Bloco
Programa: Hello.c
Data: 2026.09.22
Autor: Gabriela
*/

// importa biblioteca padrão de entrada e saída
#include <stdio.h>

//defino a função principal do tipo int
int main(){
    // printf == saída --> mostra na tela ;
    //  "entre aspas == texto ;
    //  comando se encerra por ;
    printf("Hello World!\n");

    int A=0, B=0;
    printf("Digite um valor: ");
    scanf("%d", &A);
    printf("Digite outro valor");
    scanf("%d", &B);
    int soma = A+B;
    printf("Soma: %d\n", soma);


    // indica que chegou ao fim da função == retornando 0
    return 0;
}

/*
para compilar == 
gcc <nome do arquivo> -o nome-do-programa

para exeutar ==
./nome-do-programa
*/
