#include <stdio.h>

int main(){
	int n,i;
	float x1,x2,x3,media;
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%f %f %f", &x1,&x2,&x3);
		media = (x1*2+x2*3+x3*5)/10;
		printf("%.1f\n",media);
	}
	return 0;
}
