package main

func twoSum(nums []int, target int) []int {
	first := make(map[int]int)
	second := make(map[int]int)

	for idx, num := range nums {
		_, ok := first[num]
		if ok {
			second[num] = idx
		} else {
			first[num] = idx
		}
	}

	var adj int
	var ok bool
	for num, idx := range first {
		if num+num == target {
			adj, ok = second[num]
		} else {
			adj, ok = first[target-num]
		}
		if ok {
			if idx > adj {
				idx, adj = adj, idx
			}
			return []int{idx, adj}
		}
	}

	panic("no solution")
}

func main() {
	a := twoSum([]int{3, 2, 4}, 6)
	println(a[0], a[1])
}
