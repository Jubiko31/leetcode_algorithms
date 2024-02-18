// ===========Two Sum================

func twoSum(nums []int, target int) []int {
	numbers := make(map[int]int)

	for i, a := range nums {
		b := target - a
		if j, v := numbers[b]; v {
			return []int{i, j}
		}
		numbers[a] = i
	}

	return nil
}

// Runtime: 56.99% | Memory: 59.44%