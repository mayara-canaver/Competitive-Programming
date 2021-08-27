package main

import (
	"fmt"
)

func main() {

	var izinho, jota int64 = 1, 60
	var i int64

	for i = 1; i <= 13; i++ {

		fmt.Printf("I=%d J=%d\n", izinho, jota)

		izinho += 3
		jota -= 5

	}
}
