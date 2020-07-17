#include <stdio.h>

struct hash{
	int chave;
	hash *prox;
} *def_hash;

void inserir(hash* tabela[], int pos, int n){
	hash* novo;
	novo = new hash();
	
	novo->chave = n;
	novo->prox = NULL;
	if(tabela[pos])
	{
		hash* aux = tabela[pos];
		while(aux->prox)
			aux = aux->prox;
		aux->prox = novo;
		return;
	}
	tabela[pos] = novo;
}

int funcao_hash(int num, int tam){
	return num%tam;
}


void mostra_hash(hash* tabela[], int tam){
	hash* aux;
	for(int i=0; i<tam; i++){
		aux = tabela[i];
		printf("%d", i);
		while(aux!=NULL){
			printf(" -> %d", aux->chave);
			aux = aux->prox;
		}
		printf(" -> \\");
		//if(i<tam-1)
			printf("\n");
	}
}

main(){
	int n, m, c, e;
	
	scanf("%d", &n);
	while(n--){
		scanf("%d %d", &m, &c); //m é o tam, c é a qtde de chaves
		hash* tabela[m];
		for(int i=0; i<m; i++)
			tabela[i] = NULL;
		while(c--){
			scanf("%d", &e); //recebe elemento
			inserir(tabela, funcao_hash(e, m), e);
		}
		mostra_hash(tabela, m);
		if(n>0)
			printf("\n");
	}
}
