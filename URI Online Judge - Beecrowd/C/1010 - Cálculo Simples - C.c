#include <stdio.h>
 
int main() {
 double v1, v2, total;
	int c1, c2, n1, n2;
	scanf("%d", &c1);
	scanf("%d", &n1);
	scanf("%lf", &v1);
	scanf("%d", &c2);
	scanf("%d", &n2);
	scanf("%lf", &v2);

	total = n1*v1 + n2*v2;

	printf("VALOR A PAGAR: R$ %.2lf\n", total);
	return 0;
}
