package main

import (
	"fmt"
	"math"
)

func main() {

	var vezes int
	var pa, pb, ga, gb, cresca, crescb float64

	fmt.Scanln(&vezes)

	for i := 0; i < vezes; i++ {
		var j int64 = 0

		fmt.Scanf("%f %f %f %f", &pa, &pb, &ga, &gb)

		cresca = (ga / 100) + 1
		crescb = (gb / 100) + 1

		for pa <= pb {
			pa = math.Floor(pa * cresca)
			pb = math.Floor(pb * crescb)

			j++
			if j > 100 {
				fmt.Println("Mais de 1 seculo.")
				break
			}
		}

		if j <= 100 {
			fmt.Printf("%d anos.\n", j)
		}
	}

}
