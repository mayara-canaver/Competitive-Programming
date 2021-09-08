package main

import (
	"fmt"
	"io"
)

func main() {

	var numero int

	for {
		_, err := fmt.Scanf("%d\n", &numero)

		if err == io.EOF {
			break
		}

		var slice [][]int
		for i := 0; i < numero; i++ {
			slice = append(slice, []int{})
			for j := 0; j < numero; j++ {
				if (j + i + 1) == numero {
					slice[i] = append(slice[i], 2)
				} else if j == i {
					slice[i] = append(slice[i], 1)
				} else {
					slice[i] = append(slice[i], 3)
				}
			}
		}
		for i := 0; i < numero; i++ {
			for j := 0; j < numero; j++ {
				fmt.Printf("%d", slice[i][j])
			}
			fmt.Println()

		}

	}

}
