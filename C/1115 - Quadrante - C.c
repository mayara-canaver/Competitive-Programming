#include <stdio.h>

int main(){
	int a,b;
	while((scanf("%d %d", &a, &b)) && (a != 0) && (b != 0)){
		if((a>0) && (b>0))
			printf("primeiro\n");
		else if((a>0) && (b<0))
			printf("quarto\n");
		else if((a<0) && (b>0))
			printf("segundo\n");
		else if((a<0) && (b<0))
			printf("terceiro\n");	
	}
	return 0;
}
	
