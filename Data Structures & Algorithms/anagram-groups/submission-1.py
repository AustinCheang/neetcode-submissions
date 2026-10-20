# Time: O(n * k) | Space: O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        key_dict = defaultdict(list)
        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - ord('a')] += 1
            key_dict[tuple(key)].append(s)

        for key, value in key_dict.items():
            result.append(value)

        return result