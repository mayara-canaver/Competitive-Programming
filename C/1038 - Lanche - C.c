#include <stdio.h>
 
int main() {
 int x;
	double y,valor;
	scanf("%d", &x);
	scanf("%lf", &y);
	switch(x){
		case 1:
			valor = y*4;
			printf("Total: R$ %.2lf\n",valor);
			break;
		case 2:
			valor = y*4.5;
			printf("Total: R$ %.2lf\n",valor);
			break;

		case 3:
			valor = y*5;
			printf("Total: R$ %.2lf\n",valor);
			break;

		case 4:
			valor = y*2;
			printf("Total: R$ %.2lf\n",valor);
			break;

		case 5:
			valor = y*1.5;
			printf("Total: R$ %.2lf\n",valor);
			break;

	}
	return 0;
}
