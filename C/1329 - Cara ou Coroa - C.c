#include <stdio.h>

int main(){
	int n,qtdA=0,qtdB=0,i,a;
	while(scanf("%d", &n) && (n != 0)){
		for(i=0;i<n;i++){
			scanf("%d", &a);
			if(a==0)
				qtdA++;	
			else if(a==1)
				qtdB++;
		}
		printf("Mary won %d times and John won %d times\n",qtdA,qtdB);
		qtdA = 0;
		qtdB = 0;
	}
	return 0;
}
	
