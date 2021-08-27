package main

import (
	"fmt"
)

func main() {

	var vezes float64
	var i, num_cobaia float64
	var cobaia string

	var total, total_c, total_r, total_s float64

	fmt.Scanln(&vezes)

	for i = 0; i < vezes; i++ {
		fmt.Scanf("%f %s", &num_cobaia, &cobaia)

		total += num_cobaia

		if cobaia == "C" {
			total_c += num_cobaia
		} else if cobaia == "R" {
			total_r += num_cobaia
		} else {
			total_s += num_cobaia
		}

	}

	fmt.Printf("Total: %.0f cobaias\n", total)
	fmt.Printf("Total de coelhos: %.0f\n", total_c)
	fmt.Printf("Total de ratos: %.0f\n", total_r)
	fmt.Printf("Total de sapos: %.0f\n", total_s)
	fmt.Printf("Percentual de coelhos: %.2f %%\n", total_c/total*100)
	fmt.Printf("Percentual de ratos: %.2f %%\n", total_r/total*100)
	fmt.Printf("Percentual de sapos: %.2f %%\n", total_s/total*100)

}
