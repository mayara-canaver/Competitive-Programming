package main

import "fmt"

func main() {

	var x float64
	var i int64 = 0

	fmt.Scanln(&x)

	for i < 100 {
		fmt.Printf("N[%d] = %.4f\n", i, x)

		x /= 2

		i++
	}

}
