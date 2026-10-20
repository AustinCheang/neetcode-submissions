func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }   

    var sDict[26]int

    for i := 0; i < len(s); i++ {
        sDict[s[i] - 'a']++
        sDict[t[i] - 'a']--
    }

    for _, c := range sDict {
        if c != 0 {
            return false
        }
    }
    return true
}