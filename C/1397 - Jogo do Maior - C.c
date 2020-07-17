#include <stdio.h>

int main(){
	int i,cont1=0,cont2=0,n,a,b;
	while((scanf("%d", &n)) && (n != 0)){
		for(i=0;i<n;i++){
			scanf("%d %d", &a, &b);
			if(a>b)
				cont1++;
			else if(b>a)
				cont2++;
			else if(a==b){
				
			}
		}	
		printf("%d %d\n",cont1,cont2);
		cont1 = 0;
		cont2 = 0;
	}
	return 0;
}
	
