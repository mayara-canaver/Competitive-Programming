package main

import (
	"fmt"
	"math"
)

func main() {

	var a, b, c, volume float64
	for {
		fmt.Scanln(&a, &b, &c)

		if (a + b + c) == 0 {
			break
		}

		volume = math.Floor(math.Cbrt(a * b * c))

		fmt.Println(volume)

	}
}
