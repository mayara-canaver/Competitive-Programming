#include <stdio.h>
#include <stdlib.h>

int main(){
	double n1,n2,n3,n4, media,exame,total;
	scanf("%lf", &n1);
	scanf("%lf", &n2);
	scanf("%lf", &n3);
	scanf("%lf", &n4);
	
	media = ((n1*2)+(n2*3)+(n3*4)+(n4))/10;
	printf("Media: %0.1lf\n", media);
	if(media >= 7){
		printf("Aluno aprovado.\n");
	}else if((media >= 5) && (media <7)){
		printf("Aluno em exame.\n");
		scanf("%lf", &exame);
		printf("Nota do exame: %.1lf\n", exame);
		total = (media + exame)/2;
		if(total >= 5){
			printf("Aluno aprovado.\n");
			printf("Media final: %.1lf\n", total);
		}else{
			printf("Aluno reprovado.\n");
			printf("Media final: %.1lf\n", total);
		}
	}else{
		printf("Aluno reprovado.\n");
	}
	return 0;
}
