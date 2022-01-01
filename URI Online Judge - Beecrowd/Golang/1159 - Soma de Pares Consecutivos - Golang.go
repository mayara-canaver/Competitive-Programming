package main

import "fmt"

func main() {

	var numero, total int64

	for {

		fmt.Scanln(&numero)

		if numero == 0 {
			break
		} else if numero%2 == 0 {
			total = numero + (numero + 2) + (numero + 4) + (numero + 6) + (numero + 8)
		} else {
			total = (numero + 1) + (numero + 3) + (numero + 5) + (numero + 7) + (numero + 9)
		}

		fmt.Println(total)

	}

}
