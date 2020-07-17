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

void mostraPilha(int confere){
	Celula p = celula;
	if((celula == NULL) && (confere != 1)){
		printf("correct\n");
	}else {
		printf("incorrect\n");
	}
}

int main(){
	int i,tamanho,a=1,confere;
	char expre[1001];
	while(scanf("%s", &expre) != EOF){
		criaPilha();
		tamanho = strlen(expre);
		for(i=0; i<tamanho; i++){
			if(expre[i] == '('){
				inserePilha(a);
			}else if(expre[i] == ')'){
				confere = removePilha();
				if(confere == 1){
					break;
				}else{
					continue;
				}
			}
		}
		mostraPilha(confere);
		confere = 0;
	}
	return 0;
}
