func hasDuplicate(nums []int) bool {
    visit := make(map[int]bool)
    for _, e := range nums {
        if visit[e]{
            return true
        }
        visit[e] = true
    }
    return false
}
