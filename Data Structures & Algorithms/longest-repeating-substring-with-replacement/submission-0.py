class Solution:
    # Time: O(n) | Space: O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_freq = 0

        char_counts = defaultdict(int)

        # expand the window by moving the end pointer
        for right in range(len(s)):
            right_char = s[right]
            char_counts[right_char] += 1

            max_freq = max(max_freq, char_counts[right_char])

            # check if current window is valid
            if (right - left + 1) - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
