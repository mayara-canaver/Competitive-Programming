package main

import (
	"fmt"
)

func main() {

	var n, la, lb, sa, sb int

	fmt.Scanln(&n)
	fmt.Scanln(&la, &lb)
	fmt.Scanln(&sa, &sb)

	if n >= la && n <= lb {
		if n >= sa && n <= sb {
			fmt.Println("possivel")
		} else {
			fmt.Println("impossivel")
		}
	} else {
		fmt.Println("impossivel")
	}

}
