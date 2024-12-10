package main

import (
	"fmt"
)

func main() {

	const senha = 2002

	var i int64 = 0
	var tentativa int64

	for i != 1 {

		fmt.Scanln(&tentativa)
		if tentativa == senha {
			i = 1
			fmt.Printf("Acesso Permitido\n")
		} else {
			fmt.Printf("Senha Invalida\n")
		}

	}

}
