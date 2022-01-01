package main

import (
	"fmt"
)

func main() {

	var n, c, s, numero int
	var aux, vezes int = 1, 0

	fmt.Scanln(&n, &c, &s)

	if s == 1 && aux == 1 {
		vezes++
	}

	for i := 0; i < c; i++ {

		fmt.Scanf("%d", &numero)

		aux += numero

		if aux == 0 {
			aux = n
		} else if aux > n {
			aux = 1
		}

		if aux == s {
			vezes++
		}

	}

	fmt.Println(vezes)

}
