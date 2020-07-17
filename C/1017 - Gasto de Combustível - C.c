#include <stdio.h>
 
int main() {
 int hora,km, eee;
	double combu = 12, total;
	scanf("%d", &km);
	scanf("%d", &hora);
	
	eee = hora*km;
	
	total = eee/combu;
	
	printf("%.3lf\n", total);
	return 0;
}
