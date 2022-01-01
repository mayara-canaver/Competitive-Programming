#include <stdio.h>
 
int main() {
 int i,x,cont = 0;
	scanf("%d", &x);
	
	for(i=x; i<=x+20; i++){
		if(i%2 != 0){
			cont ++;
			printf("%d\n", i);
		}
		if(cont == 6){
			break;
		}
	}
	return 0;
}
