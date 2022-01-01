#include <stdio.h>
 
int main() {
 int hi,hf,h;
	scanf("%d", &hi);
	scanf("%d", &hf);
	
	if(hi>hf){
		hi = 24-hi;
		h = hf + hi;
	}else if(hi == hf){
		h = 24;
	}else{
		h = hf - hi;
	}
	
	printf("O JOGO DUROU %d HORA(S)\n",h);
	return 0;
}
