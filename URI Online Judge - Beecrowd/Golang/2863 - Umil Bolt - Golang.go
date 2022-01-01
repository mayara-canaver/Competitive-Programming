package main

import (
	"fmt"
	"io"
)

func main() {

	var vezes int

	var aux, numero float64 = 0, 1

	for {
		_, err := fmt.Scanln(&vezes)

		if err == io.EOF {
			break
		}

		for i := 0; i < vezes; i++ {
			fmt.Scanln(&numero)

			if i == 0 {
				aux = numero
			}

			if numero < aux {
				aux = numero
			}

		}

		fmt.Println(aux)

	}

}
