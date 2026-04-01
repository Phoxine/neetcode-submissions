func hasDuplicate(nums []int) bool {
    visit := make(map[int]struct{}, len(nums))
    for _, e := range nums {
        if _, ok := visit[e]; ok{
            return true
        }
        visit[e] = struct{}{}
    }
    return false
}
