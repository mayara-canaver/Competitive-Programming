#include <stdio.h>

int main(){
	int i,n,cont=0,cont2=0,cont3=0,cont4=0;
	for(i=0;i<5;i++){
		scanf("%d", &n);
		if(n%2 == 0){
			cont++;
		}else if(n%2 != 0){
			cont2++;
		}
		if(n>0){
			cont3++;
		}else if(n<0){
			cont4++;
		}
	}
	printf("%d valor(es) par(es)\n",cont);
	printf("%d valor(es) impar(es)\n",cont2);
	printf("%d valor(es) positivo(s)\n",cont3);
	printf("%d valor(es) negativo(s)\n",cont4);

}
