/*
Disciplinha: 2026 - PCAP
Problema: beecrowd 1041 - coordenadas de um ponto
Autor: Gabriela
LIAC : le as coordenadas de um ponto no plano cartesiano,
verifica em qual quadrante ele se encontra, caso esteja em algum eixo ou na origem,
mostra a mensagem correspondente

*/

#include <stdio.h>

int main(){
    float x, y;

    scanf("%f %f", &x, &y);

    if (x == 0 && y == 0) {
        printf("Origem\n");
    } else if (x == 0) {
        printf("Eixo Y\n");
    } else if (y == 0) {
        printf ("Eixo X\n");
    } else if (x > 0 && y > 0) {
        printf("Q1\n");
    } else if (x < 0 && y > 0) {
        printf("Q2\n");
    } else if (x < 0 && y < 0) {
        printf("Q3\n");
    } else {
        printf("Q4\n");
    }

    return 0;

}