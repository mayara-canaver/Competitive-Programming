package main

import (
	"fmt"
	"math"
)

func main() {

	var vezes, count int = 0, 0
	var a, b, j float64

	fmt.Scanln(&vezes)

	for i := 0; i < vezes; i++ {
		fmt.Scanln(&a, &b)
		count = 0
		j = math.Pow(a, b)

		for j >= 1 {

			j /= 10
			count = count + 1
		}

		fmt.Println(count)

	}

}
