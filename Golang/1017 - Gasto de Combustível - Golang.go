package main

import (
	"fmt"
)

func main() {
	var tempo, velocidade float64
	var distancia float64

	fmt.Scanln(&tempo)
	fmt.Scanln(&velocidade)

	distancia = (tempo * velocidade) / 12

	fmt.Printf("%.3f\n", distancia)
}
