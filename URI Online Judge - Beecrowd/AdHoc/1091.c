#include <stdio.h>

int main(){
	int k,n,m,x,y,i;
	while((scanf("%d", &k)) && (k != 0)){
		scanf("%d %d", &n, &m);
		for(i=0;i<k;i++){
			scanf("%d %d", &x, &y);
				if((x == n) || (y == m)){
					printf("divisa\n");
				}else if(x > n){
					if(y > m)
						printf("NE\n");
					else
						printf("SE\n");
				}else if(x < n){
					if(y >m)
						printf("NO\n");
					else
						printf("SO\n");
				}
		}
	}
	return 0;
}
	
