#include <stdio.h>
#include <stdlib.h>

int main(){
	int n,i, media;
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%d", &media);
		if((media % 2 == 0) && (media > 0)){
			printf("EVEN POSITIVE\n");
		}
		if((media % 2 == 0) && (media < 0)){
			printf("EVEN NEGATIVE\n");
		}
		if((media % 2 != 0) && (media > 0)){
			printf("ODD POSITIVE\n");
		}
		if((media % 2 != 0) && (media < 0)){
			printf("ODD NEGATIVE\n");
		}
		if(media == 0){
			printf("NULL\n");
		}
	}
	
	return 0;
}
