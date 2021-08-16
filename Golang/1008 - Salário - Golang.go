package main

import "fmt"

func main() {
	var numero int
	var horas float64
	var valor_hora float64
	var salario float64
	fmt.Scanln(&numero)
	fmt.Scanln(&horas)
	fmt.Scanln(&valor_hora)
	salario = horas * valor_hora
	fmt.Printf("NUMBER = %d\n", numero)
	fmt.Printf("SALARY = U$ %.2f\n", salario)
}
