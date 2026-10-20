# Time: O(n) | Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        max_len = 0
        window = set()

        for right in range(len(s)):
            new_char = s[right]

            while new_char in window:
                window.remove(s[left])
                left += 1

            window.add(new_char)
            max_len = max(max_len, right - left + 1)

        return max_len