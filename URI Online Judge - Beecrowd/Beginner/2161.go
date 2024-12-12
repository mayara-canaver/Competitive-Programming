package main

import "fmt"

func main() {

	var vezes int
	var total float64
	var divisor float64 = 1 / 6

	fmt.Scanln(&vezes)

	if vezes == 0 {
		total = 3
		fmt.Printf("%.10f\n", total)
	} else {
		for i := 0; i < vezes; i++ {
			divisor = (1 / (6 + divisor))
		}

		total = 3 + divisor

		fmt.Printf("%.10f\n", total)
	}

}
