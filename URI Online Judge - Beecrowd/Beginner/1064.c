#include <stdio.h>

int main(){
	double n,i,soma=0,cont=0,media;
	for(i=0;i<6;i++){
		scanf("%lf", &n);
		if(n > 0){
			soma = soma + n;
			cont++;
		}
	}
	media = soma/cont;
	printf("%.0lf valores positivos\n",cont);
	printf("%.1lf\n",media);
	
	return 0;
}
