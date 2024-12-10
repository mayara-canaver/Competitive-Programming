#include <stdio.h>

int main(){
	int i,d,a=1,b=7,c=0;
	d = b;
	for(i=0;i<15;i++){
		printf("I=%d J=%d\n",a,b);
		if(c == 2){
			b = d;
			d = d + 2;
			a = a + 2;
			b = b + 2;
			c = 0;
		}else{
			b = b - 1;
			c = c + 1;
		}
		
	}
	return 0;
}
