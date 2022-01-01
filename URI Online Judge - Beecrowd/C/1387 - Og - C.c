#include <stdio.h>

int main(){
	int r,l,soma;
	while(scanf("%d %d", &l, &r) && (l != 0) && (r != 0)){
		soma = l+r;
		printf("%d\n",soma);
	}
	return 0;
}
	
