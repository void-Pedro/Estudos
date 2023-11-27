/*
** PPD / DC/UFSCar - Helio
** Programa : multiplicacao de matrizes
** Objetivo: paralelizacao om OpenMP
** Alunos: Pedro Henrique Borges - 804071
** Heitor Colichio - 800423

*/

#include <math.h>
#include <stdlib.h> 
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>

float *A, *B, *C;

int
main(int argc, char *argv[])
{
	int lin_a,col_a,lin_b,col_b,lin_c,col_c;
	int i,j,k;

	printf("Linhas A: ");   scanf("%d",&lin_a);
	printf("Colunas A / Linhas B: "); scanf("%d",&col_a);
	lin_b = col_a;
	printf("Colunas B: ");  scanf("%d",&col_b);
	printf("\n");
	lin_c = lin_a;
	col_c = col_b;

	// Alocacao dinâmica das matrizes, com linhas em sequência 
	A = (float *) malloc ( lin_a * col_a * sizeof(float) );
	B = (float *) malloc ( lin_b * col_b * sizeof(float) );
	C = (float *) malloc ( lin_c * col_c * sizeof(float) );

 	// Atribucao de valores iniciais às matrizes 
 	srand(time(NULL));

	// Opa! Vai gerar valores aleatórios em paralelo?
	// Talvez seja o caso de usar rand_r() ao invés de rand()...
  
	for(i=0; i < lin_a * col_a; i++) 
		A[i]=(float)rand() / (float)RAND_MAX; 

	for(i=0; i < lin_b * col_b; i++) 
		B[i]=(float)rand() / (float)RAND_MAX; 

	// calculo da multiplicacao
 
	// Qual/quais loop(s) paralelizar? Vale a pena paralelizar todos?
	// Tendo em vista os tempos de execução dos testes feitos acima, percebe-se que paralelizar os loops mais externos
	// é mais eficiente, já que há um salto absurdo de performance do loop intermediário para o mais interno. 

	// Qual é o efeito de fazer um parallel for em cada um dos fors abaixo?
	// Utilizando o parallel for em cada um dos loops, paraleliza-se suas iterações (dos loops aninhados também), dividindo a carga de trabalho em várias threads.

	// É necessários sincronizar alguma operação, garantindo exclusão mútua?
	// Não foi necessário, já que não havia um valor que dependia de outro

	// Paralelizando no loop mais externo
	//#pragma omp parallel for private(j,k)
	for(i=0; i < lin_c; i++) {
		
		// Paralelizando no loop intermediário
		// #pragma omp parallel for private(k)
		for(j=0; j < col_c; j++) {
			// pode ser útil usar uma variável auxiliar para os cálculos
			C[i*col_c+j]=0;

			// Paralelização no loop mais interno, testando também a utilização do reduction
			// #pragma omp parallel for
			#pragma omp parallel for reduction(+:)
			for(k=0; k < col_a; k++) 
				C[i*col_c+j] += A[i*col_a+k] * B[k*col_b+j];
       // ser usou variável auxiliar, atribui-se seu valor à C[i][j]
		}
	}

	return(0);
}


