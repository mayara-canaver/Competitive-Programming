package main

import (
	"fmt"
)

func main() {
	var pos_inicial, pos_final string
	var x1, x2, y1, y2 int

	fmt.Scanln(&pos_inicial, &pos_final)

	x1 = int(pos_inicial[0]-'a') + 1
	y1 = int(pos_inicial[1] - '0')

	x2 = int(pos_final[0]-'a') + 1
	y2 = int(pos_final[1] - '0')

	if x1+2 == x2 || x1-2 == x2 {
		if y1+1 == y2 || y1-1 == y2 {
			fmt.Println("VALIDO")
		} else {
			fmt.Println("INVALIDO")
		}
	} else if x1+1 == x2 || x1-1 == x2 {
		if y1+2 == y2 || y1-2 == y2 {
			fmt.Println("VALIDO")
		} else {
			fmt.Println("INVALIDO")
		}
	} else {
		fmt.Println("INVALIDO")
	}

}
