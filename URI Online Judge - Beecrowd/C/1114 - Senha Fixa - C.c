#include <stdio.h>

int main(){
	int senha=2002,n;
	while(n != senha){
		scanf("%d", &n);
		if(n == senha)
			break;
		printf("Senha Invalida\n");
	}printf("Acesso Permitido\n");
	return 0;
}
