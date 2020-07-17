#include <stdio.h>
 
int main() {
 int km;
	double combu, total;
	scanf("%d", &km);
	scanf("%lf", &combu);
	
	total = km/combu;
	
	printf("%.3lf km/l\n", total);
	return 0;
}
