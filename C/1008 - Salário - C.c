#include <stdio.h>
 
int main() {
 int NUMBER, HOURS;
	double X,SALARY;
	scanf("%d", &NUMBER);
	scanf("%d", &HOURS);
	scanf("%lf", &X);
	SALARY = X*HOURS;
	printf("NUMBER = %d\n", NUMBER);
	printf("SALARY = U$ %.02lf\n", SALARY);
	return 0;
}
