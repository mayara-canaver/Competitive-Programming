package main

import "fmt"

func main() {
	var numero int64
	var i int64 = 0

	var slice_par []int64
	var slice_impar []int64

	for i < 15 {

		fmt.Scanln(&numero)

		if (numero % 2) == 0 {
			if len(slice_par) == 5 {
				for j := 0; j < 5; j++ {
					fmt.Printf("par[%d] = %d\n", j, slice_par[j])
				}
				slice_par = []int64{}
			}
			slice_par = append(slice_par, numero)

		} else {
			if len(slice_impar) == 5 {
				for j := 0; j < 5; j++ {
					fmt.Printf("impar[%d] = %d\n", j, slice_impar[j])
				}
				slice_impar = []int64{}
			}
			slice_impar = append(slice_impar, numero)
		}

		i++
	}

	for j := 0; j < len(slice_impar); j++ {
		fmt.Printf("impar[%d] = %d\n", j, slice_impar[j])
	}

	for j := 0; j < len(slice_par); j++ {
		fmt.Printf("par[%d] = %d\n", j, slice_par[j])
	}

}
