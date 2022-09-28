package main

func solution(num int) string {
	var answer string
	if num%2 == 0 {
		answer = "Even"
	} else {
		answer = "Odd"
	}
	return answer
}

func main() {
	num := 3
	solution(num)
}
