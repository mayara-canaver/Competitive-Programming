#include <stdio.h>

int main() {
	float resp,N,X,Y;
	scanf("%f %f %f", &N,&X,&Y);
	resp = N/(X+Y);
	printf("%.2f\n",resp);
}
