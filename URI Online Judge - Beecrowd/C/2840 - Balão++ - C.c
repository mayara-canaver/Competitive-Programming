#include <stdio.h>

int main(){
	int R,L,qtd;
	double PI = 3.1415,volume;
	scanf("%d", &R);
	scanf("%d", &L);
	volume = ((4*PI*(R*R*R))/3);
	qtd = L/volume;
	printf("%d\n",qtd);
	return 0;
}
