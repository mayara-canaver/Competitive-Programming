package main

import (
	"fmt"
)

func main() {
	var vezes, numerico, i int64

	fmt.Scanln(&vezes, &numerico)

	for i < vezes {
		if numerico == 0 {
			fmt.Println("NULL")
		} else if numerico < 0 {

			if numerico%2 == 0 {
				fmt.Println("EVEN NEGATIVE")
			} else {
				fmt.Println("ODD NEGATIVE")
			}
		} else {

			if numerico%2 == 0 {
				fmt.Println("EVEN POSITIVE")
			} else {
				fmt.Println("ODD POSITIVE")
			}

		}

		i++
	}

}
