#include <stdio.h>
 
int main() {
 double triangulo, circulo, trapezio, quadrado, retangulo, a, b, c, pi = 3.14159;
	scanf("%lf", &a);
	scanf("%lf", &b);
	scanf("%lf", &c);

	triangulo = (a*c)/2;
	circulo = pi*(c*c);
	trapezio = (c*(a+b))/2;
	quadrado = b*b;
	retangulo = a*b;

	printf("TRIANGULO: %.3lf\n", triangulo);
	printf("CIRCULO: %.3lf\n", circulo);
	printf("TRAPEZIO: %.3lf\n", trapezio);
	printf("QUADRADO: %.3lf\n", quadrado);
	printf("RETANGULO: %.3lf\n", retangulo);
	return 0;
}
