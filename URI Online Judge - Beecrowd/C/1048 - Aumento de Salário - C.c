#include <stdio.h>

int main(){
	double salario,reajuste,total;
	scanf("%lf", &salario);
	if((salario >= 0) && (salario <= 400.00)){
		reajuste = salario*0.15;
		total = salario + reajuste;
		printf("Novo salario: %.2lf\n",total);
		printf("Reajuste ganho: %.2lf\n",reajuste);
		printf("Em percentual: 15 %%\n");
	}else if((salario >= 400.01) && (salario <= 800.00)){
		reajuste = salario*0.12;
		total = salario + reajuste;
		printf("Novo salario: %.2lf\n",total);
		printf("Reajuste ganho: %.2lf\n",reajuste);
		printf("Em percentual: 12 %%\n");
	}else if((salario >= 800.01) && (salario <= 1200.00)){
		reajuste = salario*0.10;
		total = salario + reajuste;
		printf("Novo salario: %.2lf\n",total);
		printf("Reajuste ganho: %.2lf\n",reajuste);
		printf("Em percentual: 10 %%\n");
	}else if((salario >= 1200.01) && (salario <= 2000.00)){
		reajuste = salario*0.07;
		total = salario + reajuste;
		printf("Novo salario: %.2lf\n",total);
		printf("Reajuste ganho: %.2lf\n",reajuste);
		printf("Em percentual: 7 %%\n");
	}else if(salario > 2000.00){
		reajuste = salario*0.04;
		total = salario + reajuste;
		printf("Novo salario: %.2lf\n",total);
		printf("Reajuste ganho: %.2lf\n",reajuste);
		printf("Em percentual: 4 %%\n");
	}
	return 0;
}
