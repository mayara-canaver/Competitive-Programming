package main

import (
	"fmt"
)

func main() {

	var antes, depois, total float64

	fmt.Scanf("%f %f", &antes, &depois)

	total = ((depois - antes) / antes) * 100

	fmt.Printf("%.2f%%\n", total)

}
