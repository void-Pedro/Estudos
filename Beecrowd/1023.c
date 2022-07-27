#include <stdio.h>
 
int main() {
    int n, x, y, z, cidade = 1, pessoas, menor, menori;
    float cmedio;
    
    scanf("%d", &n);
    //Enquanto o número de propriedades não for 0
    while(n != 0) {
        cmedio = 0.0;
        pessoas = 0;
        int elementos = n;
        int vetor[n][2];
        //Preenche o vetor com as informações de cada propriedade
        for(int i = 0; i < n; i++) {
            scanf("%d %d", &x, &z);
            y = z/y;
            vetor[i][0] = x;
            vetor[i][1] = y;
            cmedio += z;
            pessoas += x;
        }
        cmedio = cmedio / pessoas;
        printf("Cidade# %d:\n", cidade);
        //Enquanto ainda houver elementos no vetor de propriedades não printados
        while(elementos > 0) {
            //Acha o menor elemento
            for(int i = 0; i < n; i++) {
                if(i==0) {
                    menori = 0;
                    menor = vetor[i][1];
                }
                if(vetor[i][1] < menor) {
                    menor = vetor[i][1];
                    menori = i;
                }
            }
            printf("%d-%d", vetor[menori][0], vetor[menori][1]);
            elementos--;
            if(elementos == 0) {
                printf("\n");
            }
            printf("Consumo medio: %f m3.\n", cmedio);
            //"Retira" o elemento da lista, setando seu valor para um fora do alcance
            vetor[menori][0] = 11;
            vetor[menori][1] = 201;
        }
        cidade++;
        scanf("%d", &n);
    }
 
    return 0;
}