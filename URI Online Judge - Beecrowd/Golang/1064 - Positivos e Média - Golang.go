package main

import "fmt"

func main() {
	var variavel float64
	var contador, soma float64 = 0.0, 0.0

	for i := 0; i < 6; i++ {
		fmt.Scanf("%f", &variavel)

		if variavel >= 0 {
			contador++
			soma += variavel
		}
	}

	fmt.Printf("%.0f valores positivos\n", contador)
	fmt.Printf("%.1f\n", soma/contador)

}
