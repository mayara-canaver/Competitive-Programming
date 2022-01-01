#include <stdio.h>

int main(){
	double i,x,y,divisao;
	int n;
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%lf", &x);
		scanf("%lf", &y);
		divisao = x/y;
		if(x == 0){
			printf("0.0\n");
		}else if(y == 0){
			printf("divisao impossivel\n");
		}else{
			printf("%.1lf\n",divisao);
		}
	}
	return 0;
}
