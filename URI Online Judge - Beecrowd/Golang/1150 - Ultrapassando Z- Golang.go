package main

import "fmt"

func main() {

	var x, z, i int

	fmt.Scanln(&x)

	for {
		fmt.Scanln(&z)

		if z > x {
			for i = 1; x < z; i++ {
				x += (x + i)
			}
			fmt.Println(i + 1)
			break
		}

	}
}
