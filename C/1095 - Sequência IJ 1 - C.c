#include <stdio.h>

int main(){
	int xa=0,xe=0,xi=0,xo=0,xu=0,a=300,b=1500,c=600,d=1000,e=150,total=0;
	scanf("%d %d %d %d %d", &xa,&xe,&xi,&xo,&xu);
	total = (xa*a) + (xe*b) +(xi*c) + (xo*d) + (xu*e) + 225;
	printf("%d\n",total);
	return 0;
}
