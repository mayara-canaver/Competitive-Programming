package main

import "fmt"

func main() {

	var tronco int

	var qtd int

	fmt.Scanln(&qtd)

	for i := 0; i < qtd; i++ {

		fmt.Scanln(&tronco)

		if tronco%2 == 0 {
			fmt.Println(tronco / 2)
		} else {
			fmt.Println((tronco + 1) / 2)
		}

	}

}
