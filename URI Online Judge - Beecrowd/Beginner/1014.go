package main

import (
	"fmt"
)

func main() {
	var a, b float64
	var resultado float64

	fmt.Scanln(&a)
	fmt.Scanln(&b)

	resultado = a / b

	fmt.Printf("%.3f km/l\n", resultado)
}
