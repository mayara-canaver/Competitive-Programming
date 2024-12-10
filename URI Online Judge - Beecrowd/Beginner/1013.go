package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, c float64
	var maior_ab, resultado float64

	fmt.Scanf("%f %f %f", &a, &b, &c)

	maior_ab = (a + b + math.Abs(a-b)) / 2

	resultado = (maior_ab + c + math.Abs(maior_ab-c)) / 2

	fmt.Printf("%.0f eh o maior\n", resultado)
}
