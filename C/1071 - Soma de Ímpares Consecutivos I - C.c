#include <stdio.h>
 
int main() {
 int i,x,y,cont = 0;
	scanf("%d", &x);
	scanf("%d", &y);
	
	if(x < y){
		for(i=x+1; i<y; i++){
			if(i%2 != 0){
				cont += i;
			}
		}
				printf("%d\n", cont);
	}else{		
		for(i=y+1; i<x; i++){
			if(i%2 != 0){
				cont += i;
			}
		}
				printf("%d\n", cont);
	}
	return 0;
}
