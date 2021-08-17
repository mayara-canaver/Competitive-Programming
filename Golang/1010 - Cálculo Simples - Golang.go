package main

import (
	"fmt"
)

func main() {
	var a1, a2, a3 float64
	var b1, b2, b3 float64
	var valor float64
	fmt.Scanf("%f %f %f", &a1, &a2, &a3)
	fmt.Scanf("%f %f %f", &b1, &b2, &b3)
	valor = a2*a3 + b2*b3
	fmt.Printf("VALOR A PAGAR: R$ %.2f\n", valor)
}
