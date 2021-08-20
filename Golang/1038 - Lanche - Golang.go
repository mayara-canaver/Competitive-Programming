package main

import (
	"fmt"
)

func main() {
	total := 0.0
	var codigo, valor float64
	fmt.Scanf("%f %f", &codigo, &valor)

	if codigo == 1 {
		total = 4.0 * valor
		fmt.Printf("Total: R$ %.2f\n", total)
	} else if codigo == 2 {
		total = 4.50 * valor
		fmt.Printf("Total: R$ %.2f\n", total)
	} else if codigo == 3 {
		total = 5.0 * valor
		fmt.Printf("Total: R$ %.2f\n", total)
	} else if codigo == 4 {
		total = 2.0 * valor
		fmt.Printf("Total: R$ %.2f\n", total)
	} else if codigo == 5 {
		total = 1.50 * valor
		fmt.Printf("Total: R$ %.2f\n", total)
	} else {
		fmt.Println("Fora de intervalo")
	}

}
