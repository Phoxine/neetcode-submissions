func hasDuplicate(nums []int) bool {
    visit := make(map[int]struct{})

    for _, e := range nums{
        _, ok := visit[e]
        if ok{
            return true
        }
        visit[e] = struct{}{}
    }
    return false
}
