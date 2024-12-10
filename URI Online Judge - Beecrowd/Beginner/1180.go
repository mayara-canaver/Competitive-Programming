package main

import "fmt"

func main() {

	var vezes int
	var numero int
	var slice []int
	var aux, indexo int = 1000, 0

	fmt.Scanln(&vezes)

	for i := 0; i < vezes; i++ {

		fmt.Scanf("%d", &numero)
		slice = append(slice, numero)

	}

	for indice, v := range slice {

		if v < aux {
			aux = v
			indexo = indice
		}
	}

	fmt.Println("Menor valor:", aux)
	fmt.Println("Posicao:", indexo)

}
