package main
import "fmt"

func main() {
  var h, e, a, o, w, x int
  var bem, mal int = 0, 0
  
  fmt.Scanf("%d %d %d %d %d %d", &h, &e, &a, &o, &w, &x)

  bem = h + e + a
  mal = o + w

  if bem > mal{
    fmt.Printf("Middle-earth is safe.\n")
  }else{
    bem += x

    if bem < mal{
      fmt.Printf("Sauron has returned.\n")
    }else{
      fmt.Printf("Middle-earth is safe.\n")
    }
    
  }
  
}