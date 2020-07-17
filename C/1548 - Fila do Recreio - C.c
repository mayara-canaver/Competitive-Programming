#include <stdio.h>

int main(){
	int a,aux,m,i,n,y,pi[1000],pi2[1000],v,mais;
	
	scanf("%d", &n);
	for(i=0;i<n;i++){
		mais = 0;
		scanf("%d", &m);
		for(y=0;y<m;y++){
			scanf("%d", &pi[y]);
			pi2[y] = pi[y];	
		}
		for(a=0;a<m-1;a++){
			if(pi2[a]<pi2[a+1]){
				aux = pi2[a];
				pi2[a] = pi2[a+1];
				pi2[a+1] = aux;
				a = -1;
			}
		}
		for(v=0;v<m;v++){
			if(pi[v] == pi2[v])
				mais ++;
		}
		printf("%d\n", mais);
	}	
	return 0;
}
