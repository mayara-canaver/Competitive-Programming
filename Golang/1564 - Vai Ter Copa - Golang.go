package main

import (
	"fmt"
	"io"
)

func main() {

	var pessoa int64

	for {
		_, err := fmt.Scanf("%d", &pessoa)

		if err == io.EOF {
			break
		}

		if pessoa == 0 {
			fmt.Printf("vai ter copa!\n")
		} else {
			fmt.Printf("vai ter duas!\n")
		}

	}
}
