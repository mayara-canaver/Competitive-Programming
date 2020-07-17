#include <stdio.h>

int main(){
	int i,b=0,t1,l,c,t2;
	scanf("%d %d", &l,&c);
	t1 = (l*c) + ((l-1)*(c-1));
	if(l>1){
		for(i=1;i<l;i++){
		b = b + 2;
		}
	} 
	t2 = ((c-1)*2) + b;
	printf("%d\n%d\n",t1,t2);
	return 0;
}
