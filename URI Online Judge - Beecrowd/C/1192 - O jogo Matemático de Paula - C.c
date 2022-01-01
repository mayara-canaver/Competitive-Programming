#include <stdio.h>

int main(){
	char a;
	int n,i,x,y,total;
	scanf("%d", &n);
	for(i=0; i<n; i++){
		scanf("%d %c %d", &x, &a, &y);
		if(x == y)
			total = x*y;
		else if((a >= 'A') && (a <= 'Z'))
			total = y-x;
		else if((a >= 'a') && (a <= 'z'))
			total = x+y;
		printf("%d\n",total);
	}
	return 0;
}
	
