#include <stdio.h>

int main(){
	int a,b;
	while((scanf("%d %d", &a, &b)) && (a != b)){
		if(a>b)
			printf("Decrescente\n");
		else
			printf("Crescente\n");
	}
	return 0;
}
	
