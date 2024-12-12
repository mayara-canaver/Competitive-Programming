package main

import "fmt"

func main() {

	var vezes, numero int

	fmt.Scanln(&vezes)

	for i := 0; i < vezes; i++ {
		fmt.Scanln(&numero)

		if numero > 8000 {
			fmt.Println("Mais de 8000!")
		} else {
			fmt.Println("Inseto!")
		}

	}

}
