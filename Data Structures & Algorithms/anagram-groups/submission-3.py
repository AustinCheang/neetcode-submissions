# Time: O(n * k) | Space: O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for word in strs:
            word_idx = [0] * 26

            for char in word:
                word_idx[ord(char) - ord('a')] += 1

            anagrams_dict[tuple(word_idx)].append(word)

        return [anagrams for anagrams in anagrams_dict.values()]