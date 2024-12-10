package main

import (
	"fmt"
	"io"
	"math"
)

func main() {
	pi := 3.14

	var v, d, area, altura float64

	for {
		_, err := fmt.Scanln(&v)

		if err == io.EOF {
			break
		}

		fmt.Scanln(&d)
		area = pi * math.Pow(d/2, 2)
		altura = v / area

		fmt.Printf("ALTURA = %.2f\n", altura)
		fmt.Printf("AREA = %.2f\n", area)

	}
}
