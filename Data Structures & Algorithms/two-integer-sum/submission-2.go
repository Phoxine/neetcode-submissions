func twoSum(nums []int, target int) []int {
    // (target - num) as key, and num index as value
    need_value := make(map[int]int)

    for i, v := range nums{
        if need_index, ok :=need_value[v]; ok{
            return []int{need_index, i}
        }
        need_value[target-v] = i
    }
    return []int{}
}
