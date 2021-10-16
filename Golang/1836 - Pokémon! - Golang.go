package main

import "fmt"

func main() {

	var k int

	fmt.Scanln(&k)

	if k == 1 {
		fmt.Println("Top 1")
	} else if k <= 3 {
		fmt.Println("Top 3")
	} else if k <= 5 {
		fmt.Println("Top 5")
	} else if k <= 10 {
		fmt.Println("Top 10")
	} else if k <= 25 {
		fmt.Println("Top 25")
	} else if k <= 50 {
		fmt.Println("Top 50")
	} else {
		fmt.Println("Top 100")
	}

}
