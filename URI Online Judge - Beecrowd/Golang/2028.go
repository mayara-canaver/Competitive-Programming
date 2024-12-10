package main

import (
	"fmt"
	"io"
)

func main() {

	var vezes, seq int = 1, 0

	for {

		var alice []int
		var apar int = 1

		_, err := fmt.Scanln(&seq)

		if err == io.EOF {
			break
		} else {

			alice = append(alice, 0)

			for i := 1; i <= seq; i++ {
				for j := 0; j < i; j++ {
					alice = append(alice, i)
				}
				apar = apar + i
			}

			if seq == 0 {
				fmt.Printf("Caso %d: %d numero\n", vezes, apar)
			} else {
				fmt.Printf("Caso %d: %d numeros\n", vezes, apar)
			}

			for i, valor := range alice {
				if i == len(alice)-1 {
					fmt.Printf("%d", valor)
				} else {
					fmt.Printf("%d ", valor)
				}
			}

			fmt.Printf("\n\n")
			vezes++

		}

	}

}
