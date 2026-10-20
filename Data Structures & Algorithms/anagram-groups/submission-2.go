// Time: O(n * k) | Space: O(n * k)
func groupAnagrams(strs []string) [][]string {
    anagrams := make(map[[26]int][]string)

    for _, s := range strs {
        var key[26]int

        for _, c := range s {
            key[c - 'a']++
        }

        anagrams[key] = append(anagrams[key], s)
    }

    result := [][]string{}
    for _, value := range anagrams {
        result = append(result, value)
    }
    return result
}