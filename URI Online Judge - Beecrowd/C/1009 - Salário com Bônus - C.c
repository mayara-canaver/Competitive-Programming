#include <stdio.h>
 
int main() {
 double SALARY,COMIS, TOTAL;
	char nome[20];
	scanf("%s", &nome);
	scanf("%lf", &SALARY);
	scanf("%lf", &COMIS);
	TOTAL = SALARY+(COMIS*0.15);
	printf("TOTAL = R$ %.2lf\n", TOTAL);
	return 0;
}
