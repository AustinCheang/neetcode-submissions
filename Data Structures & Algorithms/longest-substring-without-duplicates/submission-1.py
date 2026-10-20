class Solution:
    # Time: O(n) | Space: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 0
        left = 0
        substring = set()

        for right in range(len(s)):
            right_char = s[right]

            while right_char in substring:
                substring.remove(s[left])
                left += 1

            substring.add(right_char)
            max_length = max(max_length, right - left + 1)

        return max_length