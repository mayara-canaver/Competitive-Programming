#include <stdio.h>
 
int main() {
 double bhask1,baixo, bhask2,a ,b ,c, delta;
	scanf("%lf", &a);
	scanf("%lf", &b);
	scanf("%lf", &c);
	
	baixo = 2*a;
	delta = b*b-4*a*c;
	
	bhask1 = (-b+sqrt(delta))/(baixo);
	
	bhask2 = (-b-sqrt(delta))/(baixo);
	
	if((delta < 0) || (baixo <= 0)){
		printf("Impossivel calcular\n");
	}else {
		printf("R1 = %.5lf\n",bhask1);
		printf("R2 = %.5lf\n",bhask2);
	}
	return 0;
}
