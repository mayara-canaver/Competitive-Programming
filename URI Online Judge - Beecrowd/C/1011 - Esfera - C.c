#include <stdio.h>
 
int main() {
 double raio, pi=3.14159, volume;
	scanf("%lf", &raio);
	volume = (4.0/3)*pi*(raio*raio*raio);
	printf("VOLUME = %.3lf\n", volume);
	return 0;
}
