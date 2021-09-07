package main

import "fmt"

func main() {

	var p, r int64

	fmt.Scanln(&p, &r)

	if p == 0 {
		fmt.Println("C")
	} else if r == 0 {
		fmt.Println("B")
	} else {
		fmt.Println("A")
	}

}
