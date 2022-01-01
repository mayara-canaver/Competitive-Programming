#include <stdio.h>

int main(){
	int i,a=1,b=7,c=0;
	for(i=0;i<15;i++){
		printf("I=%d J=%d\n",a,b);
		if(c == 2){
			a = a + 2;
			b = 7;
			c = 0;
		}else{
			b = b - 1;
			c = c + 1;
		}
		
	}
	return 0;
}
