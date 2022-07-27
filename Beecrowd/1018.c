#include <stdio.h>

int main() {
    int a, n;
    scanf("%d", &a);
    int vetor[7] = {100, 50, 20, 10, 5, 2, 1};
    
    printf("%d\n", a);
    for(int i = 0; i < 7; i++) {
        n = 0;
        while(a >= vetor[i]) {
            n++;
            a -= vetor[i];
        }
        printf("%d nota(s) de R$ %d,00\n", n, vetor[i]);
    }
    
    return 0;
}