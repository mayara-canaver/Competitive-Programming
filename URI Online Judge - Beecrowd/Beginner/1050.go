package main

import (
	"fmt"
)

func main() {
	var codigo int64
	fmt.Scanln(&codigo)

	switch codigo {
	case 61:
		fmt.Println("Brasilia")
	case 71:
		fmt.Println("Salvador")
	case 11:
		fmt.Println("Sao Paulo")
	case 21:
		fmt.Println("Rio de Janeiro")
	case 32:
		fmt.Println("Juiz de Fora")
	case 19:
		fmt.Println("Campinas")
	case 27:
		fmt.Println("Vitoria")
	case 31:
		fmt.Println("Belo Horizonte")
	default:
		fmt.Println("DDD nao cadastrado")
	}

}
