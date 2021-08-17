package main

import (
	"fmt"
	"math"
)

func main() {
	const pi = 3.14159
	var raio float64
	var valor float64
	fmt.Scanf("%f", &raio)
	valor = (4.0 / 3) * pi * math.Pow(raio, 3)
	fmt.Printf("VOLUME = %.3f\n", valor)
}
