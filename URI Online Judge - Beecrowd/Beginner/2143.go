package main

import "fmt"

func main() {

	var vezes, t, total int

	for {
		fmt.Scanln(&vezes)

		for i := 0; i < vezes; i++ {
			fmt.Scanln(&t)

			if t%2 == 0 {
				total = (t * 2) - 2
			} else {
				total = (t * 2) - 1
			}

			fmt.Println(total)
		}

		if vezes == 0 {
			break
		}
	}

}
