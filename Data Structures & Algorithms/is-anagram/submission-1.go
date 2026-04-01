func isAnagram(s string, t string) bool {

    if len(s) != len(t){
        return false
    }
        

    count := make(map[rune]int)
    for _, c := range s{
        count[c] ++
    }

    for _, c:= range t{
        if count[c]--; count[c] == 0{
            delete(count, c)
        }
    }
    if len(count) == 0{
        return true
    }
    return false

}
