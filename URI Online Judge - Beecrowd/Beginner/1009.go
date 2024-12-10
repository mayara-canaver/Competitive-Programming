package main

import "fmt"

func main() {
	var nome string
	var salario float64
	var vendas float64
	fmt.Scanln(&nome)
	fmt.Scanln(&salario)
	fmt.Scanln(&vendas)
	salario = salario + vendas*0.15
	fmt.Printf("TOTAL = R$ %.2f\n", salario)
}
