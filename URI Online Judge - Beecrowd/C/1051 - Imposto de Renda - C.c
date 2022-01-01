#include <stdio.h>

int main(){
	double salario,imposto=0,total;
	scanf("%lf", &salario);
	if((salario >= 0) && (salario <= 2000.00)){
		printf("Isento\n");
	}else if((salario >= 2000.01) && (salario <= 3000.00)){
		total = salario - 2000;
		imposto = total*0.08;
		printf("R$ %.2lf\n", imposto);
	}else if((salario >= 3000.01) && (salario <= 4500.00)){
		total = salario - 3000.00;
		imposto = total*0.18 + 1000*0.08;
		printf("R$ %.2lf\n", imposto);
	}else if(salario > 4500.00){
		total = salario - 4500;
		imposto = total*0.28 + 1000*0.08 + 1500*0.18;
		printf("R$ %.2lf\n", imposto);
	}
	return 0;
}
