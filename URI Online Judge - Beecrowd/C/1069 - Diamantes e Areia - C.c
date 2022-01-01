#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct reg{
	int num;
	struct reg *prox;
}*Celula;

Celula celula;

void criaPilha(){
	celula = NULL;
}

void inserePilha(int a){
	Celula aux = (Celula)malloc(sizeof(struct reg));
	aux->prox = NULL;
	aux->num = a;
	if(celula == NULL){
		celula = aux;
	}else{
		aux->prox = celula;
		celula = aux;
	}
}

int removePilha(){
	Celula p = celula;
	if(celula == NULL){
		return 1;
	}else{
		celula = celula->prox;
		free(p);
		return 0;
	}
}

int main(){
	int n,i,j,tamanho,a=1,confere,cont=0;
	char expre[1001];
	scanf("%d", &n);
	for(j=0; j<n; j++){
		scanf("%s", &expre);
		criaPilha();
		tamanho = strlen(expre);
		for(i=0; i<tamanho; i++){
			if(expre[i] == '<'){
				inserePilha(a);
			}else if(expre[i] == '>'){
				confere = removePilha();
				if(confere == 1){
					continue;
				}else{
					cont++;
				}
			}
		}
		printf("%d\n",cont);
		cont = 0;
		confere = 0;
	}
	return 0;
}
