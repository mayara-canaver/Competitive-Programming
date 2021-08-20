package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, c float64
	var total, r1, r2 float64
	fmt.Scanf("%f %f %f", &a, &b, &c)

	total = math.Pow(b, 2) - 4*a*c

	r1 = (-b + math.Sqrt(total)) / (2 * a)
	r2 = (-b - math.Sqrt(total)) / (2 * a)

	if a == 0 || total <= 0 {
		fmt.Printf("Impossivel calcular\n")
	} else {
		fmt.Printf("R1 = %.5f\n", r1)
		fmt.Printf("R2 = %.5f\n", r2)
	}

}
