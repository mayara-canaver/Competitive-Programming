package main

import "fmt"

func main() {

	var a, b, c, x, y, z, num_cont int

	fmt.Scanf("%d %d %d", &a, &b, &c)
	fmt.Scanf("%d %d %d", &x, &y, &z)

	num_cont = (x / a) * (y / b) * (z / c)
	fmt.Println(num_cont)

}
