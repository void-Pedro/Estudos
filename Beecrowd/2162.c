#include <stdio.h>
 
int main() {
    int n, status = 2, final = 1;
    scanf("%d", &n);
    int vetor[n];
    scanf("%d", &vetor[0]);
    for(int j = 1; j < n; j++) {
        scanf("%d", &vetor[j]);
        if(vetor[j-1] == vetor[j]) {
            final = 0;
        }
        if(vetor[j-1] > vetor[j]) {
            if(status == 0) {
                final = 0;
            }
            status = 0;
        } else {
            if(status == 1) {
                final = 0;
            }
            status = 1;
        }
    }
    printf("%d", final);
    return 0;
}