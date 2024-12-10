package main

import "fmt"

func main() {

	var ho, i int64

	fmt.Scanln(&ho)

	for i = 0; i < ho; i++ {
		if i == (ho - 1) {
			fmt.Printf("Ho!\n")
		} else {
			fmt.Printf("Ho ")
		}
	}

}
