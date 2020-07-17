#include <stdio.h>

int main(){
	int i,tabuada,total;
	scanf("%d", &tabuada);
	for(i=1;i<11;i++){
		total = tabuada*i;
		printf("%d x %d = %d\n",i,tabuada,total);
	}
}
