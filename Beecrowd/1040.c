#include <stdio.h>
 
int main() {
    double n1, n2, n3, n4, exame;
    scanf("%lf %lf %lf %lf", &n1, &n2, &n3, &n4);
    double media = (2.0*n1 + 3.0*n2 + 4.0*n3 + n4)/10.0;
    printf("Media: %.1lf\n", media);
    if(media >= 7.0) {  
        printf("Aluno aprovado.\n");
    } else if (media >= 5.0) {
        printf("Aluno em exame.\n");
        scanf("%lf", &exame);
        printf("Nota do exame: %.1lf\n", exame);
        media = (media + exame)/2.0;
        if(media >= 5.0) {
            printf("Aluno aprovado.\n");
        } else {
            printf("Aluno reprovado.\n");
        }
        printf("Media final: %.1lf\n", media);
    } else {
        printf("Aluno reprovado.\n");
    }
 
    return 0;
}