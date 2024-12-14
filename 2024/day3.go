package main
import (
    "fmt"
    "os"
    "regexp"
    "strconv"
    )
func day1() {
    fmt.Println("ADVENT OF CODE - DAY 3 - PART 1\nIN GO??")
    input,_:= os.ReadFile("puzzle_input.txt")
    fmt.Printf("input: %s",input)
    
    // Regex check - match then pull out the two nums so we can multiply
    pattern := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
    match := pattern.FindAllStringSubmatch(string(input),-1)
    
    var sum int = 0
    for i:=0; i<len(match);i++ {
        //fmt.Println(match[i][1], match[i][2])
        temp1, _ := strconv.Atoi(match[i][1])
        temp2, _ := strconv.Atoi(match[i][2])
        sum += (temp1 * temp2)    
    }
    fmt.Println(sum)
}

func day2() {
    fmt.Println("ADVENT OF CODE - DAY 3 - PART2\nIN GO??")
    input,_:= os.ReadFile("puzzle_input.txt")
    fmt.Printf("input: %s",input)
    
    /* Regex check - match then pull out the two nums so we can multiply
    Make two more patterns - DO and DON't. if we see do, switch bool to true.
    Only do the mult if bool is true

    Giving up on part 2 because regex is not fun :(
    */
    do_pattern := regexp.MustCompile()
    dont_pattern := regexp.MustCompile()
    
    pattern := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
    
    match := pattern.FindAllStringSubmatch(string(input),-1)
    
    var do bool = false
    var sum int = 0
    for i:=0; i<len(match);i++ {
        //fmt.Println(match[i][1], match[i][2])
        temp1, _ := strconv.Atoi(match[i][1])
        temp2, _ := strconv.Atoi(match[i][2])
        sum += (temp1 * temp2)    
    }
    fmt.Println(sum)
}
func main() {
    day1()   
    //day2()
}
