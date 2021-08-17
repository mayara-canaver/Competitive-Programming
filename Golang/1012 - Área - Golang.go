package main

import (
	"fmt"
)

func main() {
	const pi = 3.14159
	var a, b, c float64
	var triangulo, circulo, trapezio, quadrado, retangulo float64
	fmt.Scanf("%f %f %f", &a, &b, &c)

	triangulo = (a * c) / 2
	circulo = pi * c * c
	trapezio = ((a + b) * c) / 2
	quadrado = b * b
	retangulo = a * b

	fmt.Printf("TRIANGULO: %.3f\n", triangulo)
	fmt.Printf("CIRCULO: %.3f\n", circulo)
	fmt.Printf("TRAPEZIO: %.3f\n", trapezio)
	fmt.Printf("QUADRADO: %.3f\n", quadrado)
	fmt.Printf("RETANGULO: %.3f\n", retangulo)
}
