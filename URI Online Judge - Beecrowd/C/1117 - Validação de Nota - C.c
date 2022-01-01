#include <stdio.h>

int main(){
	double x,media=0,soma=0,n=0;
	while(n != 2){
		scanf("%lf", &x);
		if((x < 0) || (x > 10)){
			printf("nota invalida\n");
		}else{
			soma = soma + x;
			n++;
		}
	}
	media = soma/2;
	printf("media = %.2lf\n",media);
	return 0;
}
