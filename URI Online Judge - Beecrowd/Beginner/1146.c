#include <stdio.h>

int main(){
	int n,i;
	while(scanf("%d", &n) && n != 0){
		for(i=1;i<n+1;i++){
			if(i==n)
				printf("%d\n",i);
			else
				printf("%d ",i);
		} 
	}
	return 0;
}
