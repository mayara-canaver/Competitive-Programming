package main

import (
	"fmt"
)

func main() {

	var vezes int64

	fmt.Scanln(&vezes)

	var i int64 = 1
	var a, b float64

	for i <= vezes {

		fmt.Scanf("%f %f", &a, &b)

		if b == 0.0 {
			fmt.Printf("divisao impossivel\n")
		} else {
			fmt.Printf("%.1f\n", a/b)
		}

		i++

	}

}
