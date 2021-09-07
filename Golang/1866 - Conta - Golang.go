package main

import (
	"fmt"
)

func main() {
	var i, vezes, numero int64

	fmt.Scanln(&vezes)

	for i < vezes {

		fmt.Scanln(&numero)

		if numero%2 == 0 {
			fmt.Println(0)
		} else {
			fmt.Println(1)
		}

		i++
	}

}
