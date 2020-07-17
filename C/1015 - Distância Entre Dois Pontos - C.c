#include <stdio.h>
 
int main() {
 double x1,y1,x2,y2, total;
	scanf("%lf", &x1);
	scanf("%lf", &y1);
	scanf("%lf", &x2);
	scanf("%lf", &y2);

	total = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
	
	printf("%.4lf\n", total);
	return 0;
}
