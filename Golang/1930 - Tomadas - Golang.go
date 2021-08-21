package main

import (
	"fmt"
)

func main() {
	var t1, t2, t3, t4 int64

	var soma int64

	fmt.Scanln(&t1, &t2, &t3, &t4)

	soma = (t1 + t2 + t3 + t4) - 3

	fmt.Println(soma)

}
