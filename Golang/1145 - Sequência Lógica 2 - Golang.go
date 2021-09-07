package main

import "fmt"

func main() {

	var x, y int64
	var i, j int64
	var vezes int64

	a1 := 1

	fmt.Scanf("%d %d", &x, &y)

	vezes = y / x

	for i = 0; i < vezes; i++ {
		for j = 0; j < x; j++ {
			if j == (x - 1) {
				fmt.Printf("%d", a1)
				a1++
			} else {
				fmt.Printf("%d ", a1)
				a1++
			}
		}
		fmt.Printf("\n")
	}

}
